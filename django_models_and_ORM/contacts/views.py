from django.shortcuts import render,redirect
from contacts.models import Contact
# Create your views here.
def contact(request):
    if request.method=='POST':
    
        Contact.objects.create(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phoneNumber'),
            subject=request.POST.get('subjects'),
        )
        return redirect('/')
    return render(request, 'contact/contact.html')