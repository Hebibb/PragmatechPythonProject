from django.urls import path

from accounts.views import account,register,columnists
urlpatterns=[
    path('', account),
    path('register/', register),
    path('<int:pk>', columnists)
]