from django.contrib import admin
from .models import Food, UserInformation, BodyCircumferenceMeasurements

# Register your models here.

admin.site.register(Food)

admin.site.register(UserInformation)

admin.site.register(BodyCircumferenceMeasurements)
