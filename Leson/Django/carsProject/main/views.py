from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('If you go URL: http://127.0.0.1:8000/car/')

def car(request):
    data = {
        'c1': {
            'name': 'Audi A6 2021',
            'price': '51 000 $',
            'photo': 'main/image/audi_a6.webp'
        },
        'c2': {
            'name': 'BMW X7 2023',
            'price': '129 000 $',
            'photo': 'main/image/bmw_x7.webp'
        },
        'c3': {
            'name': 'Kia Sportage 2018',
            'price': '24 200 $',
            'photo': 'main/image/kia_sportage.webp'
        },
        'c4': {
            'name': 'Nissan X-Trail 2007',
            'price': '9 999 $',
            'photo': 'main/image/nissan_x-trail.webp'
        },
        'c5': {
            'name': 'Ford Focus 2012',
            'price': '6 900 $',
            'photo': 'main/image/ford_focus.webp'
        },
    }
    return render(request, 'car.html', {'data': data})