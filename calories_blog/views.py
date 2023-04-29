from django.shortcuts import render

# Create your views here.


def start_page(request):
    return render(request, "calories_blog/start_page.html")


def posts(request):
    pass


def single_post(request, slug):
    pass
