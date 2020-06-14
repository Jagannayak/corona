#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("<H2>HEY! Welcome to CORONA </H2>")