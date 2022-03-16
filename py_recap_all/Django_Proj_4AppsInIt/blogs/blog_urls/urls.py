from django.contrib import admin
from django.urls import path
from blogs.views import my_blogs,blog_news
urlpatterns = [
   path('',my_blogs),
   path('blog_news',blog_news)
]