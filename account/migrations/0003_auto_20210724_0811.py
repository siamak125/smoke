# Generated by Django 3.2.5 on 2021-07-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210719_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='Family',
            field=models.CharField(default=0, max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='Name',
            field=models.CharField(default=0, max_length=100, verbose_name='نام'),
        ),
    ]
