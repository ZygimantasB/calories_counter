from django.contrib import admin
from .models import ProductInformation

# Register your models here.


class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'total_fat', 'protein', 'carbohydrate']
    list_filter = ['name', 'calories', 'total_fat', 'protein', 'carbohydrate']
    search_fields = ['name']


admin.site.register(ProductInformation, ProductInformationAdmin)
