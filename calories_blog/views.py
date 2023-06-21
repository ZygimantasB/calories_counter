from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Author, Tag
from .forms import CommentForm, PostForm
# Create your views here.


class StartingPageView(ListView):
    """
    This class is responsible for displaying the starting page.
    """
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
    """
    This class is responsible for displaying all posts.
    """
    model = Post
    template_name = "calories_blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    """
    This class is responsible for displaying a single post.
    """
    def is_stored_post(self, request, post_id) -> bool:
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug) -> render:
        post = Post.objects.get(slug=slug)

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm,
            'comments': post.comments.all().order_by('-id'),
            'saved_for_later': self.is_stored_post(request, post.id)
        }
        return render(request, "calories_blog/post-detail.html", context)

    def post(self, request, slug) -> HttpResponseRedirect:
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all(),
            'saved_for_later': self.is_stored_post(request, post.id),
        }

        return render(request, "calories_blog/post-detail.html", context)


class ReadLaterView(View):
    """
    This class is responsible for displaying posts saved for later.
    """
    def get(self, request) -> render:
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = None
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, "calories_blog/stored-posts.html", context)

    def post(self, request) -> HttpResponseRedirect:
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/calories_blog/')


class PostCreateView(CreateView, LoginRequiredMixin):
    """
    This class is responsible for creating a new post.
    """
    model = Post
    template_name = 'calories_blog/post_create.html'
    fields = ['title', 'excerpt', 'image', 'content', 'author', 'tags']
    success_url = reverse_lazy('posts')

    def form_valid(self, form) -> HttpResponseRedirect:
        form.instance.slug = form.instance.title.lower().replace(' ', '-')
        return super().form_valid(form)


