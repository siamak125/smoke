from django.contrib.auth.models import User
from django.db import models


class PostModel(models.Model):
    body = models.TextField(max_length=4000)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_post")

    def __str__(self):
        return f"{self.title}: {self.body[:20]}"


# class like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     like = models.BooleanField()
