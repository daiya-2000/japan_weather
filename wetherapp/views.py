from django.http import response
import requests
from django.shortcuts import render
import math

# Create your views here.


def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid=925619e1e9cf0556f9e9c0e5892eb3db"
    city = "1861060"
    #
    r = requests.get(url.format(city)).json()

    temp = r['main']['temp'] + -273.15
    # print("日本" + response.text)
    city_weather = {
        'city': city,
        'temp': round(temp, 1),
        # [0] is List of first
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    # print(city_weather)

    context = {'city_weather': city_weather}
    return render(request, 'wetherapp/wether.html', context)
