
from django.urls import path
from base.views import blog
urlpatterns = [
  
    path('', blog)#you don't need to give path because of include in url.py
]
