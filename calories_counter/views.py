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

from .models import Food, Meal, UserInformation, BodyCircumferenceMeasurements
from .forms import FoodForm

from admin_panel_app.models import Quote

from itertools import groupby
from operator import attrgetter
from datetime import datetime
from random import choice


# Create your views here.


def start_page(request):
    image_folder = 'calories_counter/static/images/'
    image_files = os.listdir(image_folder)
    random_image = choice(image_files)
    quotes = Quote.objects.order_by('?')[:1]
    background_style = f"background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), " \
                       f"url('/static/images/{random_image}') no-repeat center center/cover;"
    context = {
        'quotes': quotes,
        'random_image': f'/static/images/{random_image}',
    }
    return render(request, "calories_counter/start_page.html", context)


class FoodsView(LoginRequiredMixin, View):
    def get(self, request):
        meals = Meal.objects.all().order_by('-date')

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

            total_macronutrients = total_values['total_protein'] + total_values['total_fat'] + total_values[
                'total_carbs']

            total_values['protein_percentage'] = (total_values['total_protein'] /
                                                  total_macronutrients * 100) if total_values['total_calories'] else 0

            total_values['fat_percentage'] = (total_values['total_fat'] /
                                              total_macronutrients * 100) if total_values['total_calories'] else 0

            total_values['carbs_percentage'] = (total_values['total_carbs'] /
                                                total_macronutrients * 100) if total_values['total_calories'] else 0

            foods_by_date.append((date, foods, total_values))

        return render(request, "calories_counter/foods.html", {"foods_by_date": foods_by_date})


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
    fields = ['meal', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']  # revert to this line
    template_name = "calories_counter/food_create.html"
    success_url = reverse_lazy('foods')

    def form_valid(self, form):
        date_str = self.request.POST.get('date')
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        meal_id = form.cleaned_data['meal'].id
        meal = Meal.objects.get(id=meal_id)
        meal.date = date
        meal.user = self.request.user
        meal.save()

        form.instance.meal = meal
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
