from django.contrib import admin
from django.urls import path
from stores.views import *
urlpatterns = [
   path('stores',my_stores),
   path('stores/offshores',offshore_strs),
   path('stores/products',my_products),
   
]