from django.shortcuts import render
from . models import Product,Brand
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import math
# Create your views here.

# @csrf_exempt
# def product_show(request):
#     products=Product.objects.all()
#     context={'products':products,}
#     #start of product likes
#     products_id=request.POST.get('product_id')

#     response=render(request, 'products/product-sticky-both.html',context)
#     liked_product=request.COOKIES.get('liked_product','')#blank is for diabling null return by get method
#     if request.method=='POST' and products_id not in liked_product:
#         response.set_cookie('liked_product',f'{liked_product},{products_id}')
        
#     return response

@csrf_exempt
def shops(request):
    #pagination
    page=request.GET.get('page',1)
    if page:
        page=int(page)  
    
    page_content=2
    all_products=Product.objects.all().count()
    pages=math.ceil(all_products/page_content)
    products=Product.objects.all()[page_content*(pages-1):(page*pages)]
    previous_page=page-1 if not page ==1 else page
    next_page=page+1 if not page==pages else page
    page_range=range(1,pages+1)
    current_page=page
    context={
        'products':products,
        'current_page':current_page,
        'previous_page':previous_page,
        'next_page':next_page,
        'page_range':page_range,
        'page':page
        }
     #likes
    products_id=request.POST.get('product_id')
   
   
    response=render(request, 'shops/shop-banner-sidebar.html',context )
    liked_product=request.COOKIES.get('liked_product','')#blank is for diabling null return by get method
    if request.method=='POST' and products_id not in liked_product:
        response.set_cookie('liked_product',f'{liked_product},{products_id}')
        #islemir heleki
    return response

   # 
    



@csrf_exempt
def product_details(request,slug):
    unit=Product.objects.filter(slug=slug)
    context={
        'unit':unit
    }
    
    products_id=request.POST.get('product_id')
    #likes
    
    response=render(request, 'products/product-sticky-both.html',context )
    liked_product=request.COOKIES.get('liked_product','')#blank is for diabling null return by get method
    if request.method=='POST' and products_id not in liked_product:
        response.set_cookie('liked_product',f'{liked_product},{products_id}')
        
    return response



    