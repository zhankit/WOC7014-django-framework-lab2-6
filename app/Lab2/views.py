import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def radarApp_view(request):
    return HttpResponse("This is the main page for Phone Radar")
