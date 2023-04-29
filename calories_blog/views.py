from django.shortcuts import render

# Create your views here.


def start_page_cal(request):
    return render(request, "calories_blog/start_page_cal.html")


def posts(request):
    return render(request, "calories_blog/all-posts.html")


def single_post(request, slug):
    pass
