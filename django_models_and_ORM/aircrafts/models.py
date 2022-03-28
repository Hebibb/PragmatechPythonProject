from django.db import models
from distutils.command.upload import upload
# Create your models here.

class Aircraft(models.Model):
  
    choices=(
    ('Onair','onair'),('Onland','onland'),
    )
   
    
    fligth_status=models.CharField(max_length=40,blank=True,null=True,default='UNKNOWN',choices=choices)
    company=models.CharField(max_length=30,default='unknown')
    plane_name=models.CharField(max_length=40,blank=True,null=True)

    about=models.TextField(max_length=300,blank=True,null=True)
    fl_score=models.IntegerField(default=0)
    model_year=models.IntegerField(default=4)
    rent_price=models.IntegerField(default=5)
    image=models.ImageField(upload_to='planePics/',blank=True,null=True)
    def __str__(self):
        
        return f'{self.plane_name} is owned by {self.company},created in {self.model_year}\n and has {self.fl_score} flight hours and is availible for hire about {self.rent_price} USD '
class Meta:
    verbose_name='Aircraft'
    verbose_name_plural='Aircrafts'
    