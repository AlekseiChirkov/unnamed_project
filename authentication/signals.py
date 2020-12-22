from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            home_address=instance.home_address,
            city=instance.city,
            region=instance.region,
            country=instance.country,
            phone=instance.phone,
            age=instance.age,
        )
        profile.save()
