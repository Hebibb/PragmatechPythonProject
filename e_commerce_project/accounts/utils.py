from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from accounts.tools.tokens import account_activation_token
User=get_user_model()
#confirmation email sent via the tools in we added in settings
def confirm_email(user_id,site_address):
    user=User.objects.filter(id=User_id)
    host_email=settings.EMAIL_HOST_USER
    guest_email=user.email#get email user input
    subject='Please confirm you registration email'
    context={
        'user':user,
        'site_Address':site_address,
        'uid':urlsafe_base64_decode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    }
    #sending email to guest email which 
    body=render_to_string('sent_emails/confirm_email.html',context)
    mail=EmailMessage(subject, to=[guest_email],host_email=host_email,body=body)
    mail.content_subtype='html'#to mail in html type
    mail.send(fail_silently=True)