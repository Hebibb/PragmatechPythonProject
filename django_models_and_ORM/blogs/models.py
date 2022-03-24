from django.db import models
from distutils.command.upload import upload
# Create your models here.
# ORM(OBJECT RELATIONAL MAPPING)
class Blog(models.Model):
    CHOICES=(('active','On'),('deactive','Off'))
    
    
   
    fullname=models.CharField( max_length=50, blank=True,null=True)
    title=models.CharField( max_length=50, blank=True)
    status=models.CharField(max_length=30, choices=CHOICES)
    content=models.TextField(max_length=20, default='UNKNOWN')
    image=models.ImageField( upload_to='blogs/',null=True,blank=True)
    published=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    price =models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.fullname}\'s books is \'{self.title}\' and price is {self.price} AZN'
class Meta:
    verbose_name='Post'
    verbose_name_plural='Posts'
    ordering=('-published_date', )#last added will be shown first
    
    
   

    
    