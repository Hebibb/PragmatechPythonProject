from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
class User(AbstractUser):
    email=models.EmailField(_('your email'),blank=True,unique=True)
    info=models.TextField(blank=True,null=True,help_text='your info if there is')
    image=models.ImageField(upload_to='users/',blank=True,null=True)
    
    
    USERNAME_FIELD = "email"#you can see in createuser command
    REQUIRED_FIELDS = ["first_name",'username']#overwrites AbstractUsers table
    
    
    
    @property
    def imageUser(self):
        if self.image:
            return self.image
        return 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'