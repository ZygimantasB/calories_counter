from django.contrib import admin
from .models import Food, Meal, FoodName, UserInformation

# Register your models here.

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(FoodName)
admin.site.register(UserInformation)
