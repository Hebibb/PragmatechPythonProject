from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    country=models.CharField(max_length=200,default='none') 
    city=models.CharField(max_length=200,) 
    street=models.CharField(max_length=200,) 
    phone=models.CharField(max_length=10,blank=True,null=True)
    rating=models.IntegerField()
    
    def __str__(self):
        return self.name