from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.views.generic import FormView

from admin_panel_app.models import ProductInformation

from .forms import ProductSearch


class ProductInformationView(FormView):
    form_class = ProductSearch
    template_name = "food_information_app/product_information.html"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_information'] = ProductInformation.objects.all()[:15]
        return self.render_to_response(context)

    def form_valid(self, form):
        query = form.cleaned_data.get("name_search")
        results = ProductInformation.objects.filter(
            Q(name__icontains=query) |
            Q(calories__icontains=query) |
            Q(protein__icontains=query) |
            Q(total_fat__icontains=query) |
            Q(carbohydrate__icontains=query)
        )
        context = {"results": results, "query": query}
        return render(self.request, "food_information_app/product_result.html", context)
