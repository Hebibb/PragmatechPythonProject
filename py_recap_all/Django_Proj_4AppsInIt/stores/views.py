from django.shortcuts import render


countries=[
    { 1:'USA',
        2:'RUSSIA',
        3:'FRANCE',
        4:'BRITAIN',},
    {1:'TURKEY',
     2:'GREECE',
     3:'SPAIN',
     4:'BELGIUM'}
]

# Create your views here.
def my_stores(request):
    return render(request,'stores.html')

def offshore_strs(request):
    context={
       'countries':countries
    }
    return render(request,'offshores.html',context=context)
def my_products(request):
    context={
        'title':'blog1',
        'content':'my content'
    }
    return render(request,'products.html',context=context)