from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    header = 'Int in profile'
    lists = ['Python', 'C++', 'Java']
    objectPerson = {'name': 'Sasha Istomin', 'age': 17}
    wedg = ('Aplle', 'Orange')

    data = {
        'header': header,
        'lists': lists,
        'objectPerson': objectPerson,
        'wedg': wedg
    }
    return render(request, 'about.html', context=data)

def user(request):
    data = {
        'name': 'Sasha'
    }
    return render(request, 'user.html', context=data)

def obj(request):
    data = {
        'name': 'Sasha',
        'age': 17
    }
    return render(request, 'obj.html', context=data)