from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá Django - index')

def ola(request):
    return HttpResponse('Olá django')