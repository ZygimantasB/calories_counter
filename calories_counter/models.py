from django.db import models
from django.conf import settings

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
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.meal} - {self.food} x {self.quantity}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Meal)
