from django.shortcuts import render
from .models import Vehicle, Vehicle_Photo

# Create your views here.
def home_view(request):
    vehicles = Vehicle.objects.all()[:8]
    vehicle_photos = Vehicle_Photo.objects.all()
    context = {'vehicles':vehicles, 'v_photos':vehicle_photos}
    return render(request, 'mainapp/index.html',context)

def about_view(request):
    return render(request, 'mainapp/about.html')

def cars_view(request):
    return render(request, 'mainapp/cars.html')

def car_details_view(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle_photos = Vehicle_Photo.objects.filter(vehicle__id=vehicle.id)
    if vehicle.dealer_discounts:
        vehicle_price = vehicle.msrp - vehicle.dealer_discounts
    else:
        vehicle_price = vehicle.msrp
    print(vehicle_price)
    context = {'vehicle':vehicle, 'v_photos':vehicle_photos, 'v_price':vehicle_price}
    return render(request, 'mainapp/car-details.html',context)

def contact_view(request):
    return render(request, 'mainapp/contact.html')