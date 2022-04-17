from django.shortcuts import render
from .models import Product,Brand
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def product_show(request):
    products=Product.objects.all()
   
    context={
        'products':products,
       
    }
  
    return render(request, 'products/product-sticky-both.html',context=context)
@csrf_exempt
def shops(request):
    return render(request,'shops/shop-fullwidth-banner.html')