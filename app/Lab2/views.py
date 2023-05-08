import random
from typing import Any
from django.db import models
# from django import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import PhoneForm
from .forms import BrandForm
from .forms import ReviewForm

from .models import Brand
from .models import Model
from .models import Review
from django.views import generic
from django.http import JsonResponse

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
    # template_name_suffix

    
    def get_queryset(self):
        # return Model.objects.all()
        brand_object = Brand.objects.get(slug=self.kwargs['slug_brand'])
        return Model.objects.filter(brand=brand_object.id)

class DetailsView(generic.DetailView):
    template_name = 'details.html'
    model = Model
    context_object_name = 'all_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        brand_object = Model.objects.get(slug=self.kwargs['slug_model'])
        context["details"] = brand_object
        return context

    # def get_queryset(self):
    #     # review_object = Model.objects.get(brand=model_object.id)
    #     brand_object = Model.objects.get(slug=self.kwargs['slug_model'])
    #     return brand_object
    #     # review_object = Model.objects.get(brand=model_object.id)
    #     # return get_details(self)
    #     # return Model.objects.get(brand=model_object.id)

def details_view(request, slug_model):
    # mymember = Model.objects.get(slug=slug)
    
    brand_object = Model.objects.get(slug=slug_model)
    # reviews_objects = Review.objects.get(model=brand_object.id)
    try: 
        reviews_objects = Review.objects.filter(model=brand_object.id)
    except:
        reviews_objects = []

    context = { 
        "details": brand_object,
        "reviews": reviews_objects
    }
    return render(request, "details.html", context)
    


class add_phone_forms_view(generic.TemplateView):
    template_name = 'addPhone.html'

    def get(self,request):
        form = PhoneForm()
        phones = Model.objects.all()
        args = {'form': form, 'phones': phones}

        return render(request, self.template_name, args)
    
    def post(self, request):
        form = PhoneForm(request.POST)
        if (form.is_valid):
            form.save()
            # title = form.cleaned_data['title']
            return HttpResponseRedirect(reverse('add_phone_forms'))



class add_brand_forms_view(generic.TemplateView):
    template_name = 'addBrand.html'

    def get(self,request):
        form = BrandForm()
        phones = Model.objects.all()
        args = {'form': form, 'phones': phones}

        return render(request, self.template_name, args)
    
    def post(self, request):
        form = BrandForm(request.POST)
        if (form.is_valid):
            form.save()
            # title = form.cleaned_data['title']
            return HttpResponseRedirect(reverse('add_phone_forms'))



class add_review_forms_view(generic.TemplateView):
    template_name = 'addReview.html'

    def get(self,request):
        form = ReviewForm()
        phones = Model.objects.all()
        args = {'form': form, 'phones': phones}

        return render(request, self.template_name, args)
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if (form.is_valid):
            form.save()
            # title = form.cleaned_data['title']
            return HttpResponseRedirect(reverse('add_phone_forms'))
