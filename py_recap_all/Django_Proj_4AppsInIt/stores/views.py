from django.shortcuts import render

# Create your views here.
def my_stores(request):
    return render(request,'stores.html')

def offshore_strs(request):
    context={
        1:'USA',
        2:'RUSSIA',
        3:'FRANCE',
        4:'BRITAIN',
    }
    return render(request,'offshores.html',context=context)
def my_products(request):
    return render(request,'products.html')