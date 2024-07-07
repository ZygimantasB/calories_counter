from django.contrib import admin
from .models import ProductInformation, Quote

# Register your models here.


class ProductInformationAdmin(admin.ModelAdmin):
    """
    This class is used to customize the admin panel for the ProductInformation model.
    """
    list_display = ['name', 'calories', 'total_fat', 'protein', 'carbohydrate']
    list_filter = ['name', 'calories', 'total_fat', 'protein', 'carbohydrate']
    search_fields = ['name']


admin.site.register(ProductInformation, ProductInformationAdmin)

admin.site.register(Quote)
