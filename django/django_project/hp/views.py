from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request): 
    return HttpResponse('<h1> Home Page </h1>')
    return HttpResponse('<!DOCTYPE html><html><head><link rel="stylesheet" href="Untitled-1.css"></head><body><h1 id="first">DISPLAY</h1><h1 id="second">DISPLAY2</h1></body></html>')
