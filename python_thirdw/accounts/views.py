from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def account(request):
    return HttpResponse('<h1 >This is my account</h1>')
def users(request):
    return render(request, 'account/salam.html')