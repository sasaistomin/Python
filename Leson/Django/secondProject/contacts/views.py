from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contacts(request):
    return HttpResponse('Contacts page')


def products(request):
    return HttpResponse('List products')

def new(request):
    return HttpResponse('New products')

def top(request):
    return HttpResponse('Top products')