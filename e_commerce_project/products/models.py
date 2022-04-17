from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.
#clothes classes starts

from vendors.models import Vendor

class Store(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
 
    
    
    
class Brand(models.Model):
    image=models.ImageField(upload_to='brands/',blank=True)
    name=models.CharField(default='Unknown', max_length=150,blank=True)
    created=models.DateField(blank=True,null=True)
   

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Brand'
        verbose_name_plural='Brands'
        ordering=('-name',)




class Product_category(models.Model):
    name=models.CharField(max_length=50,default='unknown')
    about=models.TextField(default='Nothing')
    def __str__(self):
        return self.name

class Meta:
        verbose_name='product_category'
        verbose_name_plural='product_categories'
        ordering=('-name',)


class Product(models.Model):

    choices=(('small','Small'),
             ('medium','Medium'),
             ('large','Large'),
             ('extra large','Extra Large'),
             )
    
    name=models.CharField(max_length=50,db_index=True,default='unknown')
    bar_code=models.TextField(max_length=12,unique=True,default='000000000000')
    category=models.ForeignKey('Product_category', on_delete=models.CASCADE,max_length=100,help_text='add product category')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    size=models.CharField(max_length=30,choices=choices,blank=True,null=True)
    color=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    # vendor=models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
    image1=models.ImageField(upload_to='products/')
    image2=models.ImageField(upload_to='products/')
    image3=models.ImageField(upload_to='products/')
    image4=models.ImageField(upload_to='products/')
    rating=models.IntegerField(default=0,blank=True)
    general_info=models.TextField(blank=True,null=True)
    feature1=models.TextField(blank=True,null=True)
    feature2=models.TextField(blank=True,null=True)
    feature3=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
    
