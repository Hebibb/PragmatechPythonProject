from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
class User(AbstractUser):
    email=models.EmailField(_('your email'),blank=True,unique=True)
    info=models.TextField(blank=True,null=True,help_text='your info if there is')
    image=models.ImageField(upload_to='users/',blank=True,null=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True,db_index=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True,db_index=True)
    USERNAME_FIELD = "email"#you can see in createuser command
    REQUIRED_FIELDS = ["first_name",'username']#overwrites AbstractUsers table
    
    
    
    @property
    def imageUser(self):
        if self.image:
            return self.image
        return 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'
    
class Account(models.Model):
    firstname=models.CharField(default='your name',max_length=50)
    lastname=models.CharField(help_text='your surname',max_length=50)
    email=models.EmailField(default='_@_')
    phone_number=models.CharField(max_length=10)
    image=models.ImageField(upload_to='accounts/')
    
    
    def __str__(self):
        return f'{self.firstname}\'s account'
    