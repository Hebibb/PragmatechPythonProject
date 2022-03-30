from django.db import models

# Create your models here.
#clothes classes starts
class Cl_company(models.Model):
    name=models.CharField(default='Unknown', max_length=150)
    city=models.CharField(default='Unknown', max_length=150)
    
    def __str__(self):
        return f'{self.name} is located in {self.city}'
    

class Cl_type(models.Model):
    name=models.CharField(max_length=50,)
    about=models.TextField(default='Nothing')
    def __str__(self):
        return self.name
    
class Cloth(models.Model):
    gender='M,W,UNS'
    choices=(('Small','S'),
             ('Medium','M'),
             ('Large','L'),
             ('Xlarge','XL'),
             ('XXLarge','XXL'),
             ('XXXLarger','XXXL')
             )
    
    name=models.CharField(max_length=50,blank=True)
    genders=models.CharField(max_length=10,default=gender)
    info=models.TextField(max_length=80,blank=True,null=True)
    company=models.ManyToManyField(Cl_company)
    size=models.CharField(max_length=10,choices=choices)
    cl_type=models.ForeignKey(Cl_type, on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    rating=models.IntegerField(default=0,blank=True)
    
      
       
    def __str__(self):
        
        return f'{self.company.name}\'s {self.size} {self.cl_type.name} is worth of {self.price} AZN  '