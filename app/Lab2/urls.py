"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import radarApp_view
from .views import radarApp_main_view
from .views import BrandListView
from .views import ModelListView
from .views import details_view
from django.urls import path
# from . import views

urlpatterns = [
    path("", radarApp_view, name='hw'),
    path("home", radarApp_main_view, name='hw'),
    path("brand", BrandListView.as_view(), name='brandList'),
    path("brand/<slug:slug>", ModelListView.as_view(), name='modelList'),
    path("brand/models/<slug:slug>", details_view, name='details'),
    # path('', include("HelloWorlds.urls")),
]
