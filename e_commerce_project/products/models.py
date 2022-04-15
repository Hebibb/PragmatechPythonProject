from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.
#clothes classes starts

from vendors.models import Vendor


    
    
class Brand(models.Model):
    name=models.CharField(default='Unknown', max_length=150,blank=True)
    city_address=models.CharField(default='Unknown', max_length=150,help_text='detailed address')
    list_filter=('city_address')

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



class Product(models.Model):

    choices=(('small','Small'),
             ('medium','Medium'),
             ('large','Large'),
             ('extra large','Extra Large'),
             )
    
    name=models.CharField(max_length=50,db_index=True,default='unknown')
    category=models.ForeignKey('Product_category', on_delete=models.CASCADE,max_length=100,help_text='add product category')
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    size=models.CharField(max_length=30,choices=choices)
    color=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='products')
    rating=models.IntegerField(default=0,blank=True)
    info=models.TextField(blank=True,null=True)
   
  
class Product_Features(models.Model):
    describtion=models.TextField()
    
    # @admin.display(description='Cloth amazing')
    # def amazing(self):
    #     return format_html(
    #        '<p style="color: #{};">{}</p>',
    #        'FFBF00',
    #        self.price,
    #         )
    # class Meta:
    #     verbose_name='Cloth'
    #     verbose_name_plural='Clothes'
    #     ordering=('-size',)
       
    # def __str__(self):
        
    #     return self.name