from django.shortcuts import render

from . forms import RegistrationForm
# Create your views here.
def register(request):
    # if request.POST=='POST':
    #     form=UserCreationForm()
    #     if form.is_valid():
    #         form.save()
    # messsages.success(request,'you were successfully registered',)
    
    # else:
    #     form=UserCreationForm()
    # context={
    #     'form':form
    # }
    if request.method=='POST':#if form method is post
        form=RegistrationForm(data=request.POST)
        if form.is_valid():#if form submitted
            user=form.save(commit=False)#saves form to user variable,but commit gives chance to check
            user.set_password(form.cleaned_data.get('password1'))#sets password
            user,is_active=False#send comfirmation query to your given email address
            user.save()
    context={
        'form':form
     }    
    return render(request,'login.html',context)