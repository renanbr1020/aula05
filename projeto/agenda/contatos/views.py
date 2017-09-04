from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1 (request):
    return HttpResponse ("Renan <br> João <br> Marcos")

def index (request):
    return HttpResponse ("Renan")