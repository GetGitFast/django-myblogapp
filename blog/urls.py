"""This url is similar to urls.py (django default under myblogapp folder). However, myblogapp's urls.py is project
specific and executed first. Whereas blog's urls.py is specific to the app"""

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchPostsView,
    RecentPostsView,
    AnnouncementView,
)
from . import views  # . means current path

"""For 'blog-home' route the first parameter in the path could be left blank. In the earlier versions of Django 
regular expressions were used. This is no longer required. Regular expressions were very complicated and confusing."""

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # empty string means home
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('technology/', views.technology, name='blog-technology'),
    path('knowledge/', views.knowledge, name='blog-knowledge'),
    path('oksana/', views.oksana, name='blog-oksana'),
    path('search/?', SearchPostsView.as_view(), name='search-posts'),
    path('Recent/', RecentPostsView.as_view(), name='recent-posts'),
    path('announcements/?', AnnouncementView.as_view(), name='blog-announcements'),
    path('weather/', views.weather, name='blog-weather'),
]

