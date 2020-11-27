from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )
        profile.save()