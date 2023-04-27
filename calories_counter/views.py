from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from .models import Food, MealFood, Meal


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


class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = "calories_counter/food_update.html"
    fields = ["user", "food_name", "calories"]
    success_url = reverse_lazy('foods')


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "calories_counter/food_delete.html"
    success_url = reverse_lazy('foods')


class MealFoodView(LoginRequiredMixin, View):
    def get(self, request):
        meal_foods = MealFood.objects.all()
        return render(request, "calories_counter/meal_food.html", {"meal_foods": meal_foods})


class MealFoodCreate(LoginRequiredMixin, CreateView):
    model = MealFood
    template_name = "calories_counter/meal_food_create.html"
    fields = ["meal", "food", "quantity"]
    success_url = reverse_lazy('start_page')


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    template_name = "calories_counter/meal_create.html"
    fields = "__all__"
    success_url = reverse_lazy('foods')


class MealView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = "calories_counter/meal.html"
    context_object_name = "meals"
