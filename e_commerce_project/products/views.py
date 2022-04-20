from django.shortcuts import render
from . models import Product,Brand
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.

@csrf_exempt
def product_show(request):
    products=Product.objects.all()
    context={'products':products,}
    #start of product likes
    products_id=request.POST.get('product_id')

    response=render(request, 'products/product-sticky-both.html',context)
    liked_product=request.COOKIES.get('liked_product')#blank is for diabling null return by get method
    if request.method=='POST' and products_id not in liked_product:
        response.set_cookie('liked_product',f'{liked_product},{products_id}')
        
    return response

@csrf_exempt
def shops(request):
    products=Product.objects.all()

   
    
    return render(request, 'shops/shop-banner-sidebar.html', {'products':products,})



@csrf_exempt
def product_details(request,slug):
    unit=Product.objects.filter(slug=slug)
    context={
        'unit':unit
    }
    return render(request,'products/product-swatch.html',context)


    