from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from main.forms import USerForm
# Create your views here.

persons=['Sasha', 'Oleg', 'Artem']
menu=['Home', 'About', 'Contacts']


def index(request):
    return render(request, 'index.html', context={'my_date': datetime.now()})

def list(request):
    return render(request, 'list.html', context={'menu': menu})

def postuser(request):
    # получаем из строки запроса имя пользователя
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    password = request.POST.get('password', "Undefined")
    langs = request.POST.getlist("languages", ["python"])
     
    return HttpResponse(f"""
                <div>Name: {name} <br> Age: {age} <br> Password: {password} <div>
                <br>
                <div>Languages: {langs}</div>
            """)

def reg2(request):
    userForm = USerForm()
    return render(request, 'reg2.html', {'form': userForm})