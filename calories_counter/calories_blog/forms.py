from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    This class is responsible for creating a form for adding comments.
    """
    class Meta:
        model = Comment
        fields = ("user_name", "user_email", "text")
        exclude = ("post",)
        labels = {"user_name": "Your name",
                  "user_email": "Your email",
                  "text": "Your comment"}


class PostForm(forms.ModelForm):
    """
    This class is responsible for creating a form for adding posts.
    """
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'image', 'slug', 'content', 'author', 'tags']
