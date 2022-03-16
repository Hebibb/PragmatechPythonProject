from django.shortcuts import render

# Create your views here.
def my_account(request):
    return render(request,'accounts/accounts.html')
def other_profile(request):
    return render(request,'accounts/oth_profile.html')