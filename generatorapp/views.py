from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'base.html')

def generator(request):

    alphabet = list('abcdefghiklmnopqrstvxyz')
    number = 10
    password = ''

    for i in range(number):
        password+= random.choice(alphabet)

    return render(request, 'generatorapp/home.html', {'password': password})
