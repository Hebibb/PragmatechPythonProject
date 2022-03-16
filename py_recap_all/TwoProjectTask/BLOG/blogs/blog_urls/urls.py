from django.contrib import admin
from django.urls import path,include
from blogs.views import *

urlpatterns = [
    path('', reg_sect ),
    
]
