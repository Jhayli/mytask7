from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("<p> ABOUT US </p>")

def register(request):
    return HttpResponse("<b> REGISTER HERE </b>")