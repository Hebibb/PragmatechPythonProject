from django.db import models

# Create your models here.
class Singer(models.Model):
    fullname=models.CharField(default='Unknowm',max_length=100)
    email=models.EmailField()
    bio=models.TextField(default='NONE')

    def __str__(self):
        return self.fullname
    
class Company(models.Model):
    name=models.CharField(max_length=200)
    cr_date=models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'
        ordering=('-cr_date',)

class Song(models.Model):
    
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now_add=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    ratings=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    singer=models.ManyToManyField(Singer)
    
    def __str__(self):
        return f'{self.company}\'s song namely {self.title} has rating of {self.ratings}  '
    