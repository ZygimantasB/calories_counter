import pandas as pd
from django.core.exceptions import ValidationError

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.db.models import Count

from .forms import UploadFoodInformationForm, UploadQuotesForm
from .models import ProductInformation, Quote

from calories_counter.models import Food, UserInformation
from calories_blog.models import Author, Comment, Post, Tag

from .utils import AdminPanelUtils


# Create your views here.


class UploadInformationView(LoginRequiredMixin, View):

    def get_context_data(self) -> dict:
        """
        This function is responsible for getting the context data.
        :return:
        """
        count_products = ProductInformation.objects.count()
        count_users = User.objects.count()
        count_food = Food.objects.count()
        count_meals = Food.objects.values('then_eaten').count()
        count_user_information = UserInformation.objects.count()
        count_author = Author.objects.count()
        count_comment = Comment.objects.count()
        count_post = Post.objects.count()
        count_tag = Tag.objects.count()
        count_quotes = Quote.objects.count()

        top_10_meals = Food.objects.values('then_eaten').annotate(count=Count('then_eaten')).order_by('-count')[:10]
        top_10_meals_position = list(enumerate(top_10_meals, start=1))

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

        return {
            "food_form": UploadFoodInformationForm(),
            "quotes_form": UploadQuotesForm(),
            'count_products': count_products,
            'count_users': count_users,
            'count_food': count_food,
            'count_meals': count_meals,
            'count_user_information': count_user_information,
            'count_author': count_author,
            'count_comment': count_comment,
            'count_post': count_post,
            'count_tag': count_tag,
            'user_comments_count': user_comments_count_position,
            'tag_usage': tag_usage,
            'count_quotes': count_quotes,
            'top_10_meals_position': top_10_meals_position,
        }

    def get(self, request) -> render:
        return render(request, "admin_panel_app/upload_information.html", self.get_context_data())

    def post(self, request) -> render:

        csv_validator = AdminPanelUtils()
        if "food_submit" in request.POST:
            form = UploadFoodInformationForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    csv_validator.validate_file_extension(request.FILES['file'])
                except ValidationError as error_message:
                    form.add_error('file', error_message)
                    context = self.get_context_data()
                    context.update({"food_form": form})
                    return render(request, "admin_panel_app/upload_information.html", context)
                handle_upload_food_information(request.FILES['file'])
                return redirect('upload_information')
            else:
                context = self.get_context_data()
                context.update({"food_form": form})
                return render(request, "admin_panel_app/upload_information.html", context)

        elif "quotes_submit" in request.POST:
            form = UploadQuotesForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    csv_validator.validate_file_extension(request.FILES['file'])
                except ValidationError as error_message:
                    form.add_error('file', error_message)
                    context = self.get_context_data()
                    context.update({"quotes_form": form})
                    return render(request, "admin_panel_app/upload_information.html", context)
                handle_upload_quotes(request.FILES['file'])
                return redirect('upload_information')
            else:
                context = self.get_context_data()
                context.update({"quotes_form": form})
                return render(request, "admin_panel_app/upload_information.html", context)


def handle_upload_food_information(csv_file) -> None:
    """
    This function is responsible for uploading food information to the database.
    :param csv_file:
    :return:
    """

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
    """
    This function is responsible for uploading quotes to the database.
    :param csv_file:
    :return:
    """
    read_csv = pd.read_csv(csv_file)
    for index, row in read_csv.iterrows():
        quote = Quote(
            author=row['author'],
            quote=row['quote']
        )
        quote.save()
