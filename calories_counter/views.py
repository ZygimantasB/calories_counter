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
        meals = Meal.objects.order_by('-date')
        foods_by_date = [(meal.date, Food.objects.filter(meal=meal)) for meal in meals]

        page = request.GET.get('page')
        foods = paginator.get_page(page)

        return render(request, "calories_counter/foods.html", {"foods": foods,
                                                               "foods_by_date": foods_by_date})


class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = "calories_counter/food_update.html"
    fields = '__all__'
    success_url = reverse_lazy('foods')


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "calories_counter/food_delete.html"
    success_url = reverse_lazy('foods')


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    template_name = "calories_counter/food_create.html"
    fields = '__all__'
    success_url = reverse_lazy('foods')


class UserInformationView(LoginRequiredMixin, View):

    def get(self, request):
        user_information = UserInformation.objects.all()

        return render(request, "calories_counter/user_information.html",
                      {'user_information_object': user_information})


class UserInformationCreate(LoginRequiredMixin, CreateView):
    user_information = UserInformation
    template_name = 'calories_counter/create_user_information.html'


# class UserProfileView(LoginRequiredMixin, View):
#     def get(self, request):
#         user_profiles = UserProfile.objects.all()
#         user_calories = [(profile.user.username, profile.total_calories()) for profile in user_profiles]
#         return render(request, "calories_counter/user_profile.html", {"user_calories": user_calories})
#
