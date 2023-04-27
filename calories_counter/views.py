from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Food, MealFood


# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")


class FoodView(LoginRequiredMixin, View):
    def get(self, request):
        food_objects = Food.objects.all()
        paginator = Paginator(food_objects, 10)

        page = request.GET.get('page')
        foods = paginator.get_page(page)

        return render(request, "calories_counter/food.html", {"foods": foods})


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    template_name = "calories_counter/food_create.html"
    fields = ["user", "food_name", "calories"]
    success_url = reverse_lazy('foods')


class MealFoodView(LoginRequiredMixin, View):
    def get(self, request):
        meal_foods = MealFood.objects.all()
        return render(request, "calories_counter/meal_food.html", {"meal_foods": meal_foods})


class MealFoodCreate(LoginRequiredMixin, CreateView):
    model = MealFood
    template_name = "calories_counter/meal_food_create.html"
    fields = ["meal", "food", "quantity"]
    success_url = reverse_lazy('meal_food')


# class MealFoodCreate(LoginRequiredMixin, View):
#     template_name = "calories_counter/meal_food_create.html"


# class ViewMeal(LoginRequiredMixin, View):
#     def get(self, request):
#         meals = Meal.objects.all()
#         return render(request, "calories_counter/meal.html", {"meals": meals})

