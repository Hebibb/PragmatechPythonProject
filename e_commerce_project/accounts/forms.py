from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
User=get_user_model()
from django.utils.translation import gettext_lazy as _
class RegisterForm(UserCreationForm):
    
    password1=forms.CharField(
        label=('Password',),
        widget=forms.PasswordInput(
            attrs={'autocomplete':'new password','class':'form-control','placeholder':'password'},
            ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2=forms.CharField(
        label=(' retype Password',),
        widget=forms.PasswordInput(
            attrs={'autocomplete':'new password','class':'form-control','placeholder':'comfirm password'},
            ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    
    class Meta:
        model=User
        fields=( 'first_name',
            'last_name',
            'email',
            'username',
            )
        labels={
            'first_name':'Name',
            'last_name':'Surname',
            'username':'Nickname',
            'email':"Email",
            'password1':'Password',
            'password2':'retype password',
        }   
        widgets={
            'first_name':forms.TextInput(
                attrs={'class':'form-control','placeholder':'name'},),
            'last_name':forms.TextInput(
                attrs={'class':'form-control','placeholder':'surname'},),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'},),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'nickname'},)
        }

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={
        'class':'form-group','placeholder':'email'
    }))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={
        'class':'form-group','placeholder':'password'
    }))