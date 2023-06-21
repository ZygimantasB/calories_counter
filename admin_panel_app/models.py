from django.db import models

# Create your models here.


class ProductInformation(models.Model):
    """
    This class is responsible for storing information about products.
    """
    name = models.CharField(max_length=255)
    serving_size = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=6, decimal_places=2)
    usage_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def use_product(self):
        self.usage_count += 1
        self.save()


class Quote(models.Model):
    """
    This class is responsible for storing quotes.
    """
    author = models.CharField(max_length=255, default="Unknown", blank=True, null=True)
    quote = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.quote
