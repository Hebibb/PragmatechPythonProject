from django.shortcuts import render
from blogs.models import Shareit
# Create your views here.
def sen(request):
    context={
        'title':'Blog 1',
        'header':'Tsunami'
    }
    return render(request, 'blogs.html', context=context  )
def inblog(request):
    
    return render(request, 'blogs/blogs.html' )
def auth_blogs(request):
    yazarlar=Shareit.objects.all()
    context={
        'yazarlar':yazarlar
    }
    return render(request, 'yazarlar.html',context=context)