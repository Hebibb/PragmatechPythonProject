from django.db import models
# ORM- sql kodlarinin djangoda yazilmasina komeklik eden sistemdi
#PROS ve CONS lari oyren
# blank =True datanin bos buraxilib buraxilmamasini mueyyenlesdirir
# Create your models here.
#charfielde 128 e qeder karakter girilebilir
class Shareit(models.Model):
    STATUS_CHOICES=(
        ('online','Online'),
        ('offline','Offline')
        
    )
    
    title=models.CharField(max_length=127, blank=True, null=True)
    body=models.TextField( blank=True, null=True)
    fullname=models.CharField(max_length=50, default='Unknown')
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='shares/')
    status=models.CharField(max_length=70, choices=STATUS_CHOICES)
    price=models.IntegerField(blank=True, null=True, default=0)
    
    def __str__(self):
        return f'{self.fullname}\'s {self.title} '
    