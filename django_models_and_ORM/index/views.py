from django.shortcuts import render,redirect
from index.models import Getintouch
from django.views.decorators.csrf import csrf_exempt
from .forms import GetintouchForm
from django.contrib import messages

# Create your views here.
@csrf_exempt
def getintouch(request):
    
    form=GetintouchForm()
    if request.method=='POST':
        form=GetintouchForm(data=request.POST) 
        if form.is_valid():
           form.save()
           messages.success(request, 'Profile details updated.Did you get it?')
        return redirect('/index')
    # print(request.POST)
    # if request.method=='POST':
    #     Getintouch.objects.create(#safe mode
    #         fullname=request.POST.get('fullname'),
    #         email=request.POST.get('email'),
    #         phone_number=request.POST.get('phoneNumber'),
    #         subject=request.POST.get('subjects'),
    #     )
    #     return redirect('/admin')
    return render(request, 'index/getintouch.html',{'form': form})