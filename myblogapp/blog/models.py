from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # Other options for date_posted:
    #   date_posted = models.DateTimeField(auto_now=True)
    #   - Very time a posted is updated. Good for field like last modified
    #   date_posted = models.DateTimeField(auto_now_add=True)
    #   - Only when the posted was added. Will not update in future
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # The User table has already been created by Django.
    # One user could have multiple posts. ForeignKey would make sure that only one row for User is fetched.
    # on_delete=model.CASCADE would be delete all posted in case a user is deleted.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ This will return the url redirection for PostCreateView class view defined in views.py"""
        return reverse('post-detail', kwargs={'pk': self.pk})


class Announcement(models.Model):
    """
    Model to hold global announcements
    """
    LEVEL_CHOICES = (
        ('warning', 'Warning. Be careful!'),
        ('error', 'Error. Fix it!'),
        ('success', 'Success. Let is celebrate!'),
        ('info', 'Information. No action required!'),
        ('danger', 'Danger. We are stuffed!')
    )

    heading = models.CharField(max_length=100, blank=False, default='New Announcement')
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7, choices=LEVEL_CHOICES, default='info')
    date_posted = models.DateTimeField(default=timezone.now)
    announcer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.body[:10]


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


