from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post, Author, Tag
from .forms import CommentForm
# Create your views here.


class StartingPageView(ListView):
    template_name = "calories_blog/start_page_cal.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"  # default name lists
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:5]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "calories_blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):  # slug supported by default
    # template_name = "calories_blog/post-detail.html"
    # model = Post
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        content = {
                    "post": post,
                    "post_tags": post.tags.all(),
                    "comment_form": CommentForm(),
                    "comments": post.comments.all().order_by("-id"),
                   }
        return render(request, "calories_blog/post-detail.html", content)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # create object but not save to db
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        content = {
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by("-id"),
               }

        return render(request, "calories_blog/post-detail.html", content)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context


class ReadLaterView(View):
    def post(self, request):
        stored_post = request.session.get("stored_post")

        if stored_post is None:
            stored_post = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_post:
            stored_post.append(post_id)

        request.session["stored_post"] = stored_post

        return HttpResponseRedirect("/")

    def get(self, request):
        stored_post = request.session.get("stored_post")

        context = {}

        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_post)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "calories_blog/stored-posts.html", context)





