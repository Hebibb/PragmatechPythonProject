from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
User=get_user_model()
class RegistrationForm(UserCreationForm):
    
    password1=forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(
            attrs={'autocomplete':'new password','class':'form-group','placeholder':'your password'},
            ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password1=forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(
            attrs={'autocomplete':'new password','class':'form-group','placeholder':'comfirm password'},
            ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    
    class Meta:
        model=User
        fields=(
            'first_name',
            'last_name',
            'email',
            'username',)
        widgets={
            'first_name':forms.TextInput(
                attrs={'class':'form-group','placeholder':'name'},),
            'last_namea':forms.TextInput(
                attrs={'class':'form-group','placeholder':'surname'},),
            'email':forms.EmailInput(attrs={'class':'form-group','placeholder':'email'},),
            'username':forms.TextInput(attrs={'class':'form-group','placeholder':'nickname'},)
        }