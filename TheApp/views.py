import json
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=062c4a566f9a30be0b4b89911339623b'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save() 

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon']
                } 

    context = {'weather': weather, 'form': form}
    return render(request, 'index.html', context)