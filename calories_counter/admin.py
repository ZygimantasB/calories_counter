from django.contrib import admin
from .models import Food, Meal, UserInformation

# Register your models here.

admin.site.register(Food)


class MealModelAdmin(admin.ModelAdmin):
    ordering = ['-then_eaten']


admin.site.register(Meal, MealModelAdmin)

admin.site.register(UserInformation)
