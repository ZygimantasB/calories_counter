from django.shortcuts import render
from django.db.models import Q
from django.views.generic import FormView
from django.core.paginator import Paginator

from admin_panel_app.models import ProductInformation

from .forms import ProductSearch


class ProductInformationView(FormView):
    """
    This class is responsible for displaying product information.
    """
    form_class = ProductSearch
    template_name = "food_information_app/product_information.html"

    def get(self, request, *args, **kwargs) -> render:
        paginator = Paginator(ProductInformation.objects.all(), 15)
        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)
        context['product_information'] = ProductInformation.objects.all()[:15]
        context['page_object'] = page_object
        return self.render_to_response(context)

    def form_valid(self, form) -> render:
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
