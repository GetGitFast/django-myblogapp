from django.contrib import admin
from .models import Post
from .models import Announcement
from .models import City

# Register your models here.

admin.site.register(Post)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')


admin.site.register(City)

