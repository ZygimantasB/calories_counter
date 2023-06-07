from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class UploadFoodInformationView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "food_information_app/upload_food_information.html")
