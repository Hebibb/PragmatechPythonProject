from email import message
from django.shortcuts import redirect, render,reverse
from django.urls import reverse_lazy
from . forms import RegisterForm,LoginForm
from django.contrib import messages
from accounts.utils import confirm_email
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.tools.tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
from django.conf import settings
from . models import User
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('accounts:register'))#sonraki derslerde yazilacaq
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is already activated')
        return redirect(reverse_lazy('accounts:register'))


# Create your views here.
def register(request):
    # if request.POST=='POST':
    #     form=UserCreationForm()
    #     if form.is_valid():
    #         form.save()
    # messsages.success(request,'you were successfully registered',)
    
    # else:
    #     form=UserCreationForm()
    # context={
    #     'form':form
    # }
    form=RegisterForm()
    if request.method=='POST':#if form method is post
        form=RegisterForm(data=request.POST)
        if User.objects.filter(username=username):
            messages.error(request,'This user has been already registered')
            return redirect('login')
        if User.objects.filter(email=email):
            messages.error(request,'This email has been already registered')
            return redirect('login')
        if form.is_valid():#if form submitted
            user=form.save(commit=False)#saves form to user variable,but commit gives chance to check
            user.set_password(form.cleaned_data.get('password1'))#sets password
            user.is_active=False#send comfirmation query to your given email address
            user.save()
            messsages.success(request,f'{user.first_name} {user.last_name} were successfully registered',)
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            # site_address=settings.SITE_ADDRESS
            confirm_email(user_id=user.id,site_address=site_address)
    context={
        'form':form
        }   
       
    
    return render(request,'login.html',context)
def signin(request):
    
    # if request.method=='POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
        
    #     user=authenticate(username=username,password=password)
        
    #     if user is not None:
    #         login(request, 'blog.html')
    #         fname=user.first_name
    #         context={
    #             'firstname':fname
    #         }
    #     else:
    #         messages.error(request,f'{user.username} is not participant of our site')
    #         return redirect('/login',context)
    
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(email=email,password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'You logged in ')
                return redirect(reverse_lazy('index:home'))
            else:
                messages.success(request, 'you could not make it.')
                return redirect
                                
                                
    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, 'You are signed out')
    return redirect('/login')