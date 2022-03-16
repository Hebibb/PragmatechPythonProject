
from django.urls import path,include
from blogs.views import first_blog

urlpatterns = [

    path('',first_blog)
]
