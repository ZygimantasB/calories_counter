from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

# Create your views here.


def start_page_cal(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "calories_blog/start_page_cal.html",
                  {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "calories_blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    indentified_post = get_object_or_404(Post, slug=slug)
    return render(request, "calories_blog/post-detail.html",
                  {"post": indentified_post,
                   "post_tags": indentified_post.tags.all()
    })
