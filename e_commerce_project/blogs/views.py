from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . models import Blog

# Create your views here.
@csrf_exempt
def home_blog(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request, 'blog.html',context=context)
