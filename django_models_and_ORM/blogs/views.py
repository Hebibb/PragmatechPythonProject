from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def blogs(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs,
    }
 
    return render(request, 'newblogs.html',context=context, )