from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("user_name", "user_email", "text")
        exclude = ("post",)
        labels = {"user_name": "Your name",
                  "user_email": "Your email",
                  "text": "Your comment"}
