from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, db_index=True)
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=150, db_index=True)
    home_address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone = models.CharField(max_length=16)
    age = models.DateField(null=True)

    def __str__(self):
        return self.username
