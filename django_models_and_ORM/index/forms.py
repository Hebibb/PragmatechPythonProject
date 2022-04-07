from django.forms import ModelForm
from django import forms
from . models import Getintouch
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class GetintouchForm(ModelForm):

    
    class Meta:
        model=Getintouch
        fields="__all__"
        #to change design of form in html
        widgets={
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'email@'
                    
                },
             
            ),
            'fullname': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'your name'
                }
            ),
            'subject': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'what?'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'0000000000'
                    
                }
            )
        }
def clean_email(self):
        email=self.cleaned_data['email']
        if not email.endswith('bk.ru'):
            raise ValidationError('Nar abunəsi olmayanlar daxil ola bilməz')
        else: email