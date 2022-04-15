from django.urls import path,re_path
from products.views import shops,product_show
#you have to figure out how to add two 
urlpatterns = [
    path('products/',product_show, name='products'),
    path('shops/',shops,name='shops')
]