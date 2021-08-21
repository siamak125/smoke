from django.contrib.auth.models import User
from django.db import models


class PostModel(models.Model):
    body = models.TextField(max_length=4000)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.body[:20]}"
# class comment(models.Model):
#     post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=200)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '%s - %s' % (self.post.title, self.name)
