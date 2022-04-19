from django.urls import path,re_path
from products.views import product_show,product_details,shop
#you have to figure out how to add two 
urlpatterns = [
    path('products/',product_show, name='products'),
    path('<slug:slug>',product_show, name='product_detail'),
    path('shopping/',shop,name='shopping')
  
]