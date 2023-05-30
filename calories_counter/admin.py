from django.contrib import admin
from .models import Foods, Meals, UserInformation

# Register your models here.

admin.site.register(Foods)
admin.site.register(Meals)
admin.site.register(UserInformation)
