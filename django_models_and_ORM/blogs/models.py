from django.db import models
from distutils.command.upload import upload
# Create your models here.
# ORM(OBJECT RELATIONAL MAPPING)

class Author(models.Model):
    fullname=models.CharField(default='Unknown',max_length=50, blank=True,null=True)
    age=models.IntegerField(default=18,)
    about=models.TextField(max_length=500,blank=True,null=True)

    def __str__(self):
        return f'{self.fullname} '
    
class Blog(models.Model):
    CHOICES=(('active','On'),('deactive','Off'))
    
    
   
    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    title=models.CharField( max_length=50, blank=True)
    status=models.CharField(max_length=30, choices=CHOICES)
    content=models.TextField(max_length=20, default='UNKNOWN')
    image=models.ImageField( upload_to='blogs/',null=True,blank=True)
    published=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    price =models.IntegerField(default=0)
    bloglar=models.Manager()#query edende default olan objects yerine bloglar islenecek
    def __str__(self):
        return f'{self.author}\'s books is \'{self.title}\' and price is {self.price} AZN'
    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
        ordering=('-price', )#last added will be shown first
    
    
   

    
    