from django.shortcuts import render

# Create your views here.
def sen(request):
    context={
        'title':'Blog 1',
        'header':'Tsunami'
    }
    return render(request, 'blogs.html', context=context  )
def inblog(request):
    
    return render(request, 'blogs/blogs.html' )