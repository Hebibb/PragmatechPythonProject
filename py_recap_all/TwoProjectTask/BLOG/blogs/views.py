from django.shortcuts import render

# Create your views here.
def reg_sect(request):
    return render(request, 'register.html')
def product_sect(request):
    return render(request, 'blogs/products.html')