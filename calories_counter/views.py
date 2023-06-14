import os

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

from .models import Food, UserInformation, BodyCircumferenceMeasurements

from admin_panel_app.models import Quote

from itertools import groupby
from operator import attrgetter
from random import choice
from datetime import datetime


# Create your views here.


def start_page(request):
    image_folder = 'calories_counter/static/images/'
    image_files = os.listdir(image_folder)
    random_image = choice(image_files)
    quotes = Quote.objects.order_by('?')[:1]
    context = {
        'quotes': quotes,
        'random_image': f'/static/images/{random_image}',
    }
    return render(request, "calories_counter/start_page.html", context)


class FoodsView(LoginRequiredMixin, View):
    def get(self, request):
        foods = Food.objects.filter(user=request.user).order_by('-date')

        foods_by_date = []
        for date, foods_on_date in groupby(foods, attrgetter('date')):
            foods_on_date_list = list(foods_on_date)
            total_values = {
                'total_calories': sum(food.calories for food in foods_on_date_list),
                'total_protein': sum(food.protein for food in foods_on_date_list),
                'total_fat': sum(food.fat for food in foods_on_date_list),
                'total_carbs': sum(food.carbs for food in foods_on_date_list)
            }

            total_macronutrients = total_values['total_protein'] + total_values['total_fat'] + total_values[
                'total_carbs']

            total_values['protein_percentage'] = (total_values['total_protein'] /
                                                  total_macronutrients * 100) if total_macronutrients else 0

            total_values['fat_percentage'] = (total_values['total_fat'] /
                                              total_macronutrients * 100) if total_macronutrients else 0

            total_values['carbs_percentage'] = (total_values['total_carbs'] /
                                                total_macronutrients * 100) if total_macronutrients else 0

            foods_by_date.append((date, foods_on_date_list, total_values))

        return render(request, "calories_counter/foods.html", {"foods_by_date": foods_by_date})


class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    template_name = "calories_counter/food_update.html"
    fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
    success_url = reverse_lazy('foods')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = "calories_counter/food_delete.html"
    success_url = reverse_lazy('foods')


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
    template_name = "calories_counter/food_create.html"
    success_url = reverse_lazy('foods')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserInformationView(LoginRequiredMixin, View):
    def get(self, request):

        user_information = UserInformation.objects.filter(user=request.user).first()

        paginator = Paginator(BodyCircumferenceMeasurements.objects.filter(user=request.user).order_by('-date'), 5)
        page = request.GET.get('page')
        body_volumes = paginator.get_page(page)

        return render(request, "calories_counter/user_information.html", {'user_information': user_information,
                                                                          'body_volumes': body_volumes, })


class UserInformationCreate(LoginRequiredMixin, CreateView):
    model = UserInformation
    template_name = 'calories_counter/create_user_information.html'
    fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'height', 'weight', 'gender']
    success_url = reverse_lazy('user_information')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateBodyVolumes(LoginRequiredMixin, CreateView):
    model = BodyCircumferenceMeasurements
    template_name = 'calories_counter/create_body_volumes.html'
    fields = ['neck_size', 'chest_size', 'waist_size', 'left_bicep_size', 'right_bicep_size', 'left_thigh_size',
              'left_forearm_size', 'right_forearm_size', 'left_thigh_size', 'right_thigh_size', 'left_calf_size',
              'right_calf_size']
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


class UpdateBodyVolumes(LoginRequiredMixin, UpdateView):
    model = BodyCircumferenceMeasurements
    template_name = 'calories_counter/update_body_volumes.html'
    fields = ['neck_size', 'chest_size', 'waist_size', 'left_bicep_size', 'right_bicep_size', 'left_thigh_size',
              'left_forearm_size', 'right_forearm_size', 'left_thigh_size', 'right_thigh_size', 'left_calf_size',
              'right_calf_size']
    success_url = reverse_lazy('user_information')

    def get_object(self, queryset=None):
        return get_object_or_404(BodyCircumferenceMeasurements, pk=self.kwargs.get('pk'), user=self.request.user)


class DeleteBodyVolumes(LoginRequiredMixin, DeleteView):
    model = BodyCircumferenceMeasurements
    template_name = 'calories_counter/delete_body_volumes.html'
    success_url = reverse_lazy('user_information')

    def get_object(self, queryset=None):
        return get_object_or_404(BodyCircumferenceMeasurements, pk=self.kwargs.get('pk'), user=self.request.user)
