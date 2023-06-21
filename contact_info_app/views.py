from django.shortcuts import render

# Create your views here.


def contact_info(request):
    return render(request, "contact_info_app/contact_info.html")
