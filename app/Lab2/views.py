import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def radarApp_view(request):
    context = {"greetings": "Welcome to week 4 - The Views"}
    return render(request, "base.html", context)

def radarApp_main_view(request):
    return render(request, "mainPage.html")

def phoneList_view(request):
    return render(request, "child.html")
