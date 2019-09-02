""" This signal will get fired after an object is saved. We want to get a post_save signal when a new user is created.
    User model in this case is the sender of the signal. We also need to define the receiver signal. A receiver signal
    is function that gets this signal and then performs some task.
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


