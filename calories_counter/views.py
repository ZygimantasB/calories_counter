from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

from django.views.generic.list import ListView

from django.forms.models import inlineformset_factory

from extra_views import CreateWithInlinesView, InlineFormSetFactory

from .models import Food, Meal, UserInformation

from itertools import groupby
from operator import attrgetter
from datetime import datetime


# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")


class FoodsView(LoginRequiredMixin, View):
    def get(self, request):
        meals = Meal.objects.all()

        foods_by_date = []
        for date, meals_on_date in groupby(meals, attrgetter('date')):
            foods = Food.objects.filter(meal__in=meals_on_date, user=request.user)
            total_values = foods.aggregate(
                total_calories=Coalesce(Sum('calories'), 0, output_field=DecimalField()),
                total_protein=Coalesce(Sum('protein'), 0, output_field=DecimalField()),
                total_fat=Coalesce(Sum('fat'), 0, output_field=DecimalField()),
                total_carbs=Coalesce(Sum('carbs'), 0, output_field=DecimalField())
            )

            print(total_values)

            total_protein = total_values.get('total_protein', 0)
            total_fat = total_values.get('total_fat', 0)
            total_carbs = total_values.get('total_carbs', 0)

            print(total_protein, total_fat, total_carbs)

            total_macronutrients = total_values['total_protein'] + total_values['total_fat'] + total_values['total_carbs']

            total_values['protein_percentage'] = (total_values['total_protein'] / total_macronutrients * 100) if total_values['total_calories'] else 0
            total_values['fat_percentage'] = (total_values['total_fat'] / total_macronutrients * 100) if total_values['total_calories'] else 0
            total_values['carbs_percentage'] = (total_values['total_carbs'] / total_macronutrients * 100) if total_values['total_calories'] else 0
            foods_by_date.append((date, foods, total_values))

        #TODO paginator are usless at this time don`t forget to delete it later
        paginator = Paginator(Food.objects.filter(user=request.user), 10)
        page = request.GET.get('page')
        foods = paginator.get_page(page)

        return render(request, "calories_counter/foods.html", {"foods": foods,
                                                               "foods_by_date": foods_by_date})


class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = "calories_counter/food_update.html"
    fields = ['meal', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
    success_url = reverse_lazy('foods')

    def form_valid(self, form):
        form.instance.meal.date = self.request.POST.get('date')
        return super().form_valid(form)


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "calories_counter/food_delete.html"
    success_url = reverse_lazy('foods')


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['meal', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
    template_name = "calories_counter/food_create.html"
    success_url = reverse_lazy('foods')

    def form_valid(self, form):
        date_str = self.request.POST.get('date')
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        meal = Meal.objects.create(date=date, user=self.request.user, then_eaten=form.cleaned_data['meal'].then_eaten)

        form.instance.meal = meal
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserInformationView(LoginRequiredMixin, View):
    def get(self, request):
        user_information = UserInformation.objects.filter(user=request.user).first()

        return render(request, "calories_counter/user_information.html", {'user_information': user_information})


class UserInformationCreate(LoginRequiredMixin, CreateView):
    model = UserInformation
    template_name = 'calories_counter/create_user_information.html'
    fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'height', 'weight', 'gender']
    success_url = reverse_lazy('user_information')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserInformationUpdate(LoginRequiredMixin, UpdateView):
    model = UserInformation
    template_name = 'calories_counter/update_user_information.html'
    fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'height', 'weight', 'gender']
    success_url = reverse_lazy('user_information')

    def get_object(self, queryset=None):
        return get_object_or_404(UserInformation, user=self.request.user)
