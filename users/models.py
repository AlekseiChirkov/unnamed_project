import jwt
import datetime

from datetime import datetime, timedelta
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.core.mail import EmailMultiAlternatives
from django_rest_passwordreset.signals import reset_password_token_created


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise TypeError("Please, enter your email.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    DoesNotExist = None
    USER_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=16, choices=USER_GENDER)
    phone = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    avatar = models.ImageField(upload_to='media/users/avatars')
    is_banned = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def token(self):
        return self._generate_jwt_token()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "http://localhost:8000/change-password/?token={token}".format(token=reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('users/user_reset_password.html', context)
    email_plaintext_message = render_to_string('users/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()


@receiver(post_save, sender=User)
def banned_notifications(sender, instance, created, **kwargs):
    if instance.is_banned:
        instance.is_active = False
        mail_subject = 'Your account has been banned | Vrmates team'
        message = render_to_string('users/account_ban.html', {
            'user': instance.first_name
        })
        to_email = instance.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
