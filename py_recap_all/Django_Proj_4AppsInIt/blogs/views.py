from django.shortcuts import render

# Create your views here.
def my_blogs(request):
    return render(request,'blogs/blogs.html')
def blog_news(request):
    context={
        'author':'Karen Filipova',
        'title':'Future of Developing',
        'publish_date':'02.05.2020',
    }
    return render(request,'blogs/blog_news.html',context=context)