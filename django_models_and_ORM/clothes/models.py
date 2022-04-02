from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
# Create your models here.
#clothes classes starts

class Tax_Office(models.Model):
    address=models.CharField(max_length=200,default='place')
    TIN=models.CharField(max_length=10,unique=True,error_messages={'unique':_("this number already exists")})
    
    def __str__(self):
        return self.TIN
    

    
    
class Cl_company(models.Model):
    name=models.CharField(default='Unknown', max_length=150,blank=True)
    city_address=models.CharField(default='Unknown', max_length=150,help_text='detailed address')
    list_filter=('city_address')
    TIN=models.OneToOneField('Tax_Office', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Textile Company'
        verbose_name_plural='Textile Companies'
        ordering=('-name',)




class Cl_type(models.Model):
    name=models.CharField(max_length=50,default='unknown')
    about=models.TextField(default='Nothing')
    def __str__(self):
        return self.name


class Store(models.Model):
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    link=models.URLField(max_length=200)   
    
    def __str__(self):
        return f'{self.title} is in {self.address}. For further info {self.link} '

class Cloth(models.Model):

    choices=(('Small','S'),
             ('Medium','M'),
             ('Large','L'),
             ('Xlarge','XL'),
             ('XXLarge','XXL'),
             ('XXXLarger','XXXL')
             )
    
    name=models.CharField(max_length=50,db_index=True,default='unknown')
    genders=models.CharField(max_length=10,help_text='Men,Women,Unisex')
    info=models.TextField(max_length=80,blank=True,null=True)
    company=models.ManyToManyField(Cl_company)
    size=models.CharField(max_length=10,choices=choices)
    cl_type=models.ForeignKey(Cl_type, on_delete=models.CASCADE,related_name='clothes')
    price=models.IntegerField(default=0)
    rating=models.IntegerField(default=0,blank=True)
    stores=models.ManyToManyField('Store')
  
    
    
    @admin.display(description='Cloth amazing')
    def amazing(self):
        return format_html(
           '<p style="color: #{};">{}</p>',
           'FFBF00',
           self.price,
            )
    class Meta:
        verbose_name='Cloth'
        verbose_name_plural='Clothes'
        ordering=('-size',)
       
    def __str__(self):
        
        return self.name