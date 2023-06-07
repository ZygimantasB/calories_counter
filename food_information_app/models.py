from django.db import models

# Create your models here.


class ProductInformation(models.Model):
    name = models.CharField(max_length=255)
    serving_size = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_protein = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=6, decimal_places=2)
    total_carbohydrate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    