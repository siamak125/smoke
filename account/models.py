from django.db import models
from django.contrib.auth.models import User

status_choice = ((1, "مرد"), (2, "زن"))


class profileModel(models.Model):
    Gender = models.IntegerField(choices=status_choice, verbose_name="جنسیت ")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربری", related_name="profile")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"
