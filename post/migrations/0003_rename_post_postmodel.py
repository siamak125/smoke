# Generated by Django 3.2.5 on 2021-08-14 10:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20210814_0954'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='PostModel',
        ),
    ]