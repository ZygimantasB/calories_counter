from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Count

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} commented {self.text[:20]} on {self.post}"

    def get_user_comments_count(self):
        user_comments_count = Comment.objects.values('user_name').annotate(count=Count('user_name')).order_by('-count')
        return user_comments_count
