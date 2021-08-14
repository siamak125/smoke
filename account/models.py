from django.db import models
from django.contrib.auth.models import User

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


