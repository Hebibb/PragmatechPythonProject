from django.urls import path,re_path
from products.views import product_details,shops
#you have to figure out how to add two 
urlpatterns = [
    # path('products/',product_show, name='products'),
    # path('products/<slug:slug>',product_show, name='product_detail'),
    path('shopping/',shops,name='shopping'),
    path('<slug:slug>',product_details, name='slugit')
  
]