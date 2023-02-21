from django.shortcuts import render, get_object_or_404
from .models import car

# Create your views here.
def cars(request):
    teams = car.objects.all()
    return render(request, 'cars/cars.html' ,{'teams':teams} )

def car_details(request,id):
    single_car = get_object_or_404(car, pk=id)
    data = {
        'single_car':single_car
    }
    return render(request, 'cars/car_details.html', data)
