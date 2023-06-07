import pandas as pd

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UploadFoodInformationForm
from .models import ProductInformation

# Create your views here.


class UploadFoodInformationView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFoodInformationForm()
        return render(request, "food_information_app/upload_food_information.html", {"form": form})

    def post(self, request):
        form = UploadFoodInformationForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return redirect('upload_food_information')  #TODO chage redirect dont forget
        else:
            return render(request, "food_information_app/upload_food_information.html", {"form": form})


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
