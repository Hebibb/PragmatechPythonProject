from django.contrib import admin
from django.urls import path
from blogs.views import my_blogs,blog_news,blog_details
urlpatterns = [
   path('',my_blogs, name='blog'),
   path('blognews/',blog_news,name='blognew'),
   path('<int:blog>',blog_details,name='details')
]