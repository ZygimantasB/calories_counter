from django.shortcuts import render
from .models import Food
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")


class FoodView(View):
    def get(self, request):
        food_objects = Food.objects.all()
        paginator = Paginator(food_objects, 10)

        page = request.GET.get('page')
        foods = paginator.get_page(page)

        return render(request, "calories_counter/food.html", {"foods": foods})

