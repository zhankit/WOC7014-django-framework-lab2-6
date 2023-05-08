from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Brand
from .models import Model
from .models import Review

# class BrandAdmin(admin.ModelAdmin):
#     list_display = ("name","origin")
#     prepopulated_fields = {"slug": ("name")} 


admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Review)