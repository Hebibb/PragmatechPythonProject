from django.db import models

# Create your models here.
class Store(models.Model):
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    link=models.URLField(max_length=200)   
    
    def __str__(self):
        return f'{self.title} is in {self.address}. For further info {self.link} '