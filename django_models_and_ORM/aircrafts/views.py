from django.shortcuts import render
from aircrafts.models import Aircraft
# Create your views here.
# Create your views here.
def air(request):
    airline=Aircraft.objects.all()
    context={
        'Airline':airline,
    }
    return render(request,'aircrafts/aircraft.html',context=context)