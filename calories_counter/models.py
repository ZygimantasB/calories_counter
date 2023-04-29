from django.db import models
from django.conf import settings
from django.db.models import Sum, F

# Create your models here.


class Food(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    calories = models.FloatField()

    def __str__(self):
        return self.food_name


class Meal(models.Model):
    meal_name = models.CharField(max_length=255)
    foods = models.ManyToManyField(Food, through="MealFood")

    def __str__(self):
        return self.meal_name


class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.meal} - {self.food} x {self.quantity}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)

    def total_calories(self):
        total = 0
        for meal in self.meals.all():
            total += meal.foods.through.objects.filter(meal=meal).annotate(
                total_calories=F('food__calories') * F('quantity')
            ).aggregate(sum_calories=Sum('total_calories'))['sum_calories'] or 0
        return total

