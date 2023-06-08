import pandas as pd

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import UploadFoodInformationForm
from .models import ProductInformation

from calories_counter.models import Food, Meal, UserInformation
from calories_blog.models import Author, Comment, Post, Tag


# Create your views here.


class UploadFoodInformationView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFoodInformationForm()
        count_products = ProductInformation.objects.count()
        count_users = User.objects.count()
        count_food = Food.objects.count()
        count_meal = Meal.objects.count()
        count_user_information = UserInformation.objects.count()
        count_author = Author.objects.count()
        count_comment = Comment.objects.count()
        count_post = Post.objects.count()
        count_tag = Post.objects.count()

        top_10_products = ProductInformation.objects.order_by('-usage_count')[:10]
        top_10_products_position = list(enumerate(top_10_products, start=1))

        return render(request, "food_information_app/upload_food_information.html",
                      {"form": form,
                       'count_products': count_products,
                       'count_users': count_users,
                       'count_food': count_food,
                       'count_meal': count_meal,
                       'count_user_information': count_user_information,
                       'count_author': count_author,
                       'count_comment': count_comment,
                       'count_post': count_post,
                       'count_tag': count_tag,
                       'top_10_products': top_10_products_position,


                       }
                      )

    def post(self, request):
        form = UploadFoodInformationForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return redirect('upload_food_information')  #TODO chage redirect dont forget
        else:
            return render(request, "food_information_app/upload_food_information.html", {"form": form})


class DetailDatabaseInformation(LoginRequiredMixin, View):
    def get(self, request):
        count_products = ProductInformation.objects.count()
        count_users = User.objects.count()
        return render(request, "food_information_app/count_information.html",
                      {'count_products': count_products,
                       'count_users': count_users},
                      )


def handle_upload_file(csv_file):
    read_csv = pd.read_csv(csv_file)
    for index, row in read_csv.iterrows():
        product_information = ProductInformation(
            name=row['name'],
            serving_size=row['serving_size'],
            calories=row['calories'],
            total_fat=row['total_fat'],
            protein=row['protein'],
            carbohydrate=row['carbohydrate']
        )
        product_information.save()


