from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'generatorapp/home.html')

def generator(request):
    return HttpResponse("Сыр сөздү жаратуу барагы")
