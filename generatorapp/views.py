from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Салам, бул сайттын биринчи барагы")

def generator(request):
    return HttpResponse("Сыр сөздү жаратуу барагы")
