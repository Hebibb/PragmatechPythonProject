from django.urls import path

from accounts.views import account,register
urlpatterns=[
    path('', account),
    path('register/', register)
]