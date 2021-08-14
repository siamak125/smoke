from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    body = RichTextField(blank=True, null=True, verbose_name="کامنت")
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()


class comment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
