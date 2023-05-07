import random
# from django import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand
from .models import Model
from django.views import generic
# Create your views here.

def radarApp_view(request):
    context = {"greetings": "Welcome to week 4 - The Views"}
    return render(request, "base.html", context)

def radarApp_main_view(request):
    return render(request, "mainPage.html")

class BrandListView(generic.ListView):
    template_name = 'brandList.html'
    context_object_name = 'all_brands'

    def get_queryset(self):
            return Brand.objects.all()

class ModelListView(generic.ListView):
    template_name = 'modelList.html'
    context_object_name = 'all_models'
    
    def get_queryset(self):
        return Model.objects.all()

def details_view(request, slug):
    # mymember = Model.objects.get(slug=slug)
    context = { "details": "mymember"}
    return render(request, "details.html", context)
    