# Generated by Django 4.2 on 2023-05-08 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab2', '0004_brand_slug_model_slug_review_slug_alter_brand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
    ]