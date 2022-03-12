from django.urls import path
from blogs.views import sen
from blogs.views import auth_blogs
urlpatterns=[
    path('men/', sen),
    path('yazarlar/', auth_blogs)
]