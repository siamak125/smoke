from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

status_choice = ((1, "مرد"), (2, "زن"))


class profileModel(models.Model):
    Gender = models.IntegerField(choices=status_choice, verbose_name="جنسیت ")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربری", related_name="profile",
                                default=None)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"


class passwordResetModel(models.Model):
    uid = models.UUIDField(default=None, verbose_name="شناسه")
    date = models.DateTimeField(verbose_name="تاریخ", auto_now=True)
    email = models.EmailField(default=None)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()


class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
