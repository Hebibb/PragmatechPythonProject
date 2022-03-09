from django.shortcuts import render

# Create your views here.

#functional base view

def blogs(request):
    
    return render(request, 'blog/blog.html')
