from django.shortcuts import render

# Create your views here.
def product_show(request):
    return render(request, 'products/product-sticky-both.html')
def shops(request):
    return render(request,'shops/shop-fullwidth-banner.html')