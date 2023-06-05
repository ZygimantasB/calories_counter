from django.db import models

from django.contrib.auth.models import User

from datetime import date

from CONSTATNS.gender import GENDER
from CONSTATNS.then_eaten import THEN_EATEN

# Create your models here.


class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)
    name = models.ManyToManyField('FoodName', related_name='food_name', blank=True, null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    weight_measure = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name.name


class FoodName(models.Model):
    name = models.CharField(max_length=255)
    food = models.ForeignKey('Food', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    then_eaten = models.CharField(max_length=50, choices=THEN_EATEN, default='Snack')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.then_eaten


class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=6, choices=GENDER)
    user_photo = models.ImageField(blank=True, null=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            born = self.date_of_birth
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Food(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     food_name = models.CharField(max_length=255)
#     calories = models.FloatField()
#
#     def __str__(self):
#         return self.food_name
#
#
# class Meal(models.Model):
#     meal_name = models.CharField(max_length=255)
#     foods = models.ManyToManyField(Food, through="MealFood")
#
#     def __str__(self):
#         return self.meal_name
#
#
# class MealFood(models.Model):
#     meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)
#     quantity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.meal} - {self.food} x {self.quantity}"
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     meals = models.ManyToManyField(Meal)
#
#     def total_calories(self):
#         total = 0
#         for meal in self.meals.all():
#             total += meal.foods.through.objects.filter(meal=meal).annotate(
#                 total_calories=F('food__calories') * F('quantity')
#             ).aggregate(sum_calories=Sum('total_calories'))['sum_calories'] or 0
#         return total


