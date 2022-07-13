from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'base.html')

def generator(request):

    alphabet = list('abcdefghiklmnopqrstvxyz')
    number = int(request.GET.get('length', 12))
    password = ''

    if request.GET.get('uppercase'):
        alphabet.extend(list('ABCDEFGHIKLMNOPQRSTVXYZ'))
    
    if request.GET.get('numbers'):
        alphabet.extend(list('0123456789'))

    if request.GET.get('special'):
        alphabet.extend(list('!@#$%^&*'))

    for i in range(number):
        password+= random.choice(alphabet)

    return render(request, 'generatorapp/home.html', {'password': password})

def about(request):
    return render(request, "generatorapp/about.html")
