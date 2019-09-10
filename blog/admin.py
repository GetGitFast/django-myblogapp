from django.contrib import admin
from .models import Post
from .models import Announcement
from .models import City


""" These would override Django default on the Admin page"""
admin.site.site_header = "myblogapp Admin"
admin.site.site_title = "myblogapp Admin Area"
admin.site.index_title = "Welcome to the myblogapp admin area"

# Register your models here.

admin.site.register(Post)
admin.site.register(City)
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('body', 'level', 'display')




