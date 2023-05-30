from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from django.forms import inlineformset_factory

from .models import Food, Meal, FoodName, UserInformation
from .forms import FoodForm, MealForm


# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")


class FoodsView(LoginRequiredMixin, View):
    def get(self, request):
        food_objects = Food.objects.all()
        paginator = Paginator(food_objects, 10)

        page = request.GET.get('page')
        foods = paginator.get_page(page)

        return render(request, "calories_counter/foods.html", {"foods": foods})


class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = "calories_counter/food_update.html"
    fields = '__all__'
    success_url = reverse_lazy('foods')


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "calories_counter/food_delete.html"
    success_url = reverse_lazy('foods')


class FoodCreate(LoginRequiredMixin, View):
    template_name = "calories_counter/food_create.html"

    def get(self, request):
        food_form = FoodForm()
        meal_formset = inlineformset_factory(Meal, form=MealForm, extra=1)
        return render(request, "calories_counter/food_create.html", {"food_form": food_form})

    def post(self, request):
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            return redirect('foods')
        return render(request, "calories_counter/food_create.html", {"food_form": food_form})



# class FoodView(LoginRequiredMixin, View):
#     def get(self, request):
#         food_objects = Food.objects.all()
#         paginator = Paginator(food_objects, 10)
#
#         page = request.GET.get('page')
#         foods = paginator.get_page(page)
#
#         return render(request, "calories_counter/foods.html", {"foods": foods})
#
#
# class FoodCreate(LoginRequiredMixin, CreateView):
#     model = Food
#     template_name = "calories_counter/food_create.html"
#     fields = ["user", "food_name", "calories"]
#     success_url = reverse_lazy('foods')
#
#
# class FoodUpdate(LoginRequiredMixin, UpdateView):
#     model = Food
#     template_name = "calories_counter/food_update.html"
#     fields = ["user", "food_name", "calories"]
#     success_url = reverse_lazy('foods')
#
#
# class FoodDelete(LoginRequiredMixin, DeleteView):
#     model = Food
#     template_name = "calories_counter/food_delete.html"
#     success_url = reverse_lazy('foods')
#
#
# class MealFoodView(LoginRequiredMixin, View):
#     def get(self, request):
#         meal_foods = MealFood.objects.all()
#         return render(request, "calories_counter/meal_food.html", {"meal_foods": meal_foods})
#
#
# class MealFoodCreate(LoginRequiredMixin, CreateView):
#     model = MealFood
#     template_name = "calories_counter/meal_food_create.html"
#     fields = ["meal", "food", "quantity"]
#     success_url = reverse_lazy('start_page')
#
#
# class MealFoodUpdate(LoginRequiredMixin, UpdateView):
#     model = MealFood
#     template_name = "calories_counter/meal_food_update.html"
#     fields = ["meal", "food", "quantity"]
#     success_url = reverse_lazy('meal_food')
#
#
# class MealFoodDelete(LoginRequiredMixin, DeleteView):
#     model = MealFood
#     template_name = "calories_counter/meal_food_delete.html"
#     success_url = reverse_lazy('meal_food')
#
#
# class MealCreate(LoginRequiredMixin, CreateView):
#     model = Meal
#     template_name = "calories_counter/meal_create.html"
#     fields = "__all__"
#     success_url = reverse_lazy('foods')
#
#
# class MealView(LoginRequiredMixin, ListView):
#     model = Meal
#     template_name = "calories_counter/meal.html"
#     context_object_name = "meals"
#
#
# class MealUpdate(LoginRequiredMixin, UpdateView):
#     model = Meal
#     template_name = "calories_counter/meal_update.html"
#     fields = "__all__"
#     success_url = reverse_lazy('meals')
#
#
# class MealDelete(LoginRequiredMixin, DeleteView):
#     model = Meal
#     template_name = "calories_counter/meal_delete.html"
#     success_url = reverse_lazy('meals')
#
#
# class UserProfileView(LoginRequiredMixin, View):
#     def get(self, request):
#         user_profiles = UserProfile.objects.all()
#         user_calories = [(profile.user.username, profile.total_calories()) for profile in user_profiles]
#         return render(request, "calories_counter/user_profile.html", {"user_calories": user_calories})
#
