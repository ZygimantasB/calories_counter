import pandas as pd

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.db.models import Count

from .forms import UploadFoodInformationForm, UploadQuotesForm
from .models import ProductInformation, Quote

from calories_counter.models import Food, UserInformation
from calories_blog.models import Author, Comment, Post, Tag


# Create your views here.

class UploadInformationView(LoginRequiredMixin, View):
    def get(self, request) -> render:

        count_quotes = Quote.objects.count()

        food_form = UploadFoodInformationForm()
        quotes_form = UploadQuotesForm()
        count_products = ProductInformation.objects.count()
        count_users = User.objects.count()
        count_food = Food.objects.count()
        count_user_information = UserInformation.objects.count()
        count_author = Author.objects.count()
        count_comment = Comment.objects.count()
        count_post = Post.objects.count()
        count_tag = Tag.objects.count()

        top_10_products = ProductInformation.objects.order_by('-usage_count')[:10]
        top_10_products_position = list(enumerate(top_10_products, start=1))

        user_comments_count = Comment.objects.values('user_name').annotate(count=Count('user_name')).order_by('-count')
        user_comments_count_position = list(enumerate(user_comments_count, start=1))[:10]

        top_tags_count = Post.objects.annotate(num_tags=Count('tags'))
        top_tags_count_position = list(enumerate(top_tags_count, start=1))[:10]

        posts = Post.objects.all()
        tag_usage = {}
        for post in posts:
            tags = post.tags.all()
            for tag in tags:
                if tag.caption in tag_usage:
                    tag_usage[tag.caption] += 1
                else:
                    tag_usage[tag.caption] = 1

        tag_usage = dict(sorted(tag_usage.items(), key=lambda value: value[1], reverse=True))
        tag_usage = dict(list(tag_usage.items())[:10])

        return render(request, "admin_panel_app/upload_information.html", {
            "food_form": food_form,
            "quotes_form": quotes_form,
            'count_products': count_products,
            'count_users': count_users,
            'count_food': count_food,
            'count_user_information': count_user_information,
            'count_author': count_author,
            'count_comment': count_comment,
            'count_post': count_post,
            'count_tag': count_tag,
            'top_10_products': top_10_products_position,
            'user_comments_count': user_comments_count_position,
            'tag_usage': tag_usage,
            'count_quotes': count_quotes,
        })

    def post(self, request) -> render:
        if "food_submit" in request.POST:
            form = UploadFoodInformationForm(request.POST, request.FILES)
            if form.is_valid():
                handle_upload_food_information(request.FILES['file'])
                return redirect('upload_information')
            else:
                return render(request, "admin_panel_app/upload_information.html", {"food_form": form})
        elif "quotes_submit" in request.POST:
            form = UploadQuotesForm(request.POST, request.FILES)
            if form.is_valid():
                handle_upload_quotes(request.FILES['file'])
                return redirect('upload_information')
            else:
                return render(request, "admin_panel_app/upload_information.html", {"quotes_form": form})


class DetailDatabaseInformation(LoginRequiredMixin, View):
    def get(self, request) -> render:
        count_products = ProductInformation.objects.count()
        count_users = User.objects.count()
        return render(request, "admin_panel_app/count_information.html",
                      {'count_products': count_products,
                       'count_users': count_users},
                      )


def handle_upload_food_information(csv_file) -> None:
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


def handle_upload_quotes(csv_file) -> None:
    read_csv = pd.read_csv(csv_file)
    for index, row in read_csv.iterrows():
        quote = Quote(
            author=row['author'],
            quote=row['quote']
        )
        quote.save()

