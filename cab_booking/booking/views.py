# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Cab, Ride

def home(request):
    cabs = Cab.objects.filter(available=True)
    return render(request, 'booking/home.html', {'cabs': cabs})

def book_ride(request, cab_id):
    if request.method == 'POST':
        cab = Cab.objects.get(id=cab_id)
        customer_name = request.POST['customer_name']
        pickup_location = request.POST['pickup_location']
        dropoff_location = request.POST['dropoff_location']
        Ride.objects.create(
            customer_name=customer_name,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            cab=cab
        )
        cab.available = False
        cab.save()
        return redirect('home')
    return render(request, 'booking/book_ride.html', {'cab_id': cab_id})
