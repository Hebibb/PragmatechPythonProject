from django.db import models

# Create your models here.
class Getintouch(models.Model):
    fullname=models.CharField(default='your name',max_length=50)
    email=models.CharField(default='_@_',max_length=100,)
    phone_number=models.CharField(max_length=10)
    subject=models.TextField(max_length=255)

    
    
    def __str__(self):
        return f'{self.fullname}\'s info'