# Generated by Django 4.2 on 2023-05-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab2', '0005_remove_brand_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
