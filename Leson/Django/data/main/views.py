from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from main.forms import USerForm
from .models import Person
from .models import Auto
import asyncio
# Create your views here.

persons=['Sasha', 'Oleg', 'Artem']
menu=['Home', 'About', 'Contacts']


def index(request):
    return render(request, 'index.html', context={'my_date': datetime.now()})

# def list(request):
#     return render(request, 'list.html', context={'menu': menu})

# def postuser(request):
#     # получаем из строки запроса имя пользователя
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     password = request.POST.get('password', "Undefined")
#     langs = request.POST.getlist("languages", ["python"])
     
#     return HttpResponse(f"""
#                 <div>Name: {name} <br> Age: {age} <br> Password: {password} <div>
#                 <br>
#                 <div>Languages: {langs}</div>
#             """)

# def reg2(request):
#     userForm = USerForm()
#     return render(request, 'reg2.html', {'form': userForm})

async def acreate_person():
    person = await Person.objects.acreate(name="Sasha", age=17)
    print(person.name)

asyncio.run(acreate_person())

def get_person(request):
    # получаем все объекты Person из базы данных
    persons = Person.objects.all()
    # формируем строку с информацией о каждом объекте Person
    response_text = ""
    for person in persons:
        response_text += f"Name: {person.name}, Age: {person.age}<br>"
    return HttpResponse(response_text)

def setCar(request):
    listCar = Auto.objects.bulk_create([
        Auto(name='Mercedes-Benz GL-Class 2012', engine=4.66, ear=2012, color='Чорний'),
        Auto(name='Audi A6 2021', engine=2.97, ear=2021, color='Білий')
        ])
    return HttpResponse('das')