from django.shortcuts import render
from django.views import View
from django.db.models import Q

from admin_panel_app.models import ProductInformation

from .forms import ProductSearch

# Create your views here.


class ProductInformationView(View):
    def get(self, request):
        form_class = ProductSearch
        product_information = ProductInformation.objects.all()
        context = {"product_information": product_information}
        return render(request, "food_information_app/product_information.html", context=context)

    def form_valid(self, form):
        query = form.cleaned_data.get("query")
        result = ProductInformation.objects.filter(food_name__icontains="apple")
        context = {"result": result, "query": query, }
        return render(self.request, "food_information_app/product_result.html", context=context)
