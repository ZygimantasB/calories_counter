from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.forms.models import inlineformset_factory

from extra_views import CreateWithInlinesView, InlineFormSetFactory
"""

"""


from .models import Food, Meal, FoodName, UserInformation


# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")


class FoodsView(LoginRequiredMixin, View):
    def get(self, request):
        food_objects = Food.objects.filter(user=request.user)
        paginator = Paginator(food_objects, 10)
        meals = Meal.objects.filter(user=request.user).order_by('-date')
        foods_by_date = [(meal.date, Food.objects.filter(meal=meal, user=request.user)) for meal in meals]

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


class FoodNameInline(InlineFormSetFactory):
    model = FoodName
    fields = ['name']


class FoodCreate(LoginRequiredMixin, CreateWithInlinesView):
    model = Food
    inlines = [FoodNameInline]
    fields = ['meal', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
    template_name = "calories_counter/food_create.html"
    success_url = reverse_lazy('foods')

    def forms_valid(self, form, inlines):
        form.instance.user = self.request.user
        return super().forms_valid(form, inlines)


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
