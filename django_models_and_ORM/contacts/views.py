from django.shortcuts import render,redirect
from contacts.models import Contact
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def contact(request):
    if request.method=='POST':
        Contact.objects.create(#unsafe mode
            firstname=request.GET.get('firstname'),
            lastname=request.GET.get('lastname'),
            email=request.GET.get('email'),
            phone_number=request.GET.get('phoneNumber'),
            subject=request.GET.get('subjects'),
        )
        return redirect('/')
    return render(request, 'contact/contact.html')