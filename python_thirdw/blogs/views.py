from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#functional base view
def blog(request):
    return HttpResponse('My blog')