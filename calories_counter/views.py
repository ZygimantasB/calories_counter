from django.shortcuts import render

# Create your views here.


def start_page(request):
    return render(request, "calories_counter/start_page.html")
