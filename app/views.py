from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def rentalbike(request):
    if request.method=='POST':
        bn=request.POST['bn']
        cn=request.POST['cn']
        rp=request.POST.get('rp')

        BO=rent.objects.get_or_create(bike_name=bn,customer_name=cn,bike_rent=rp)[0]
        BO.save()

        return HttpResponse('Bike rented Successfully')

    return render(request,'rentalbike.html')