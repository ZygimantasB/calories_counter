from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Food
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

