# Generated by Django 4.2 on 2023-05-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab2', '0002_brand_model_remove_review_date_remove_review_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
