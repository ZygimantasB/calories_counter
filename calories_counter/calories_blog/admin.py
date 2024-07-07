from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """
    This class is used to customize the admin panel for the Post model.
    """
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")


class CommentAdmin(admin.ModelAdmin):
    """
    This class is used to customize the admin panel for the Comment model.
    """
    list_display = ("user_name", "user_email", "post")
    list_filter = ("user_name", "user_email", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
