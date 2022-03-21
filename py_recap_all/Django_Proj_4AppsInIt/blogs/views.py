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
def blog_details(request, blog):
    blogs=[{
        1: {
        'author':'Karen Filipova',
        'title':'Future of Developing',
        'publish_date':'02.05.2020', 
        },
       2: {
        'author':'Yuri Kalkin',
        'title':'Jungle',
        'publish_date':'02.06.2010', 
        }
    }
       
    ]
    blog=blogs[0][blog]#
    return render(request, 'blogs/details.html',{'blog':blog})