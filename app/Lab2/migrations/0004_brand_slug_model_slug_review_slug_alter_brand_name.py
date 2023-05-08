# Generated by Django 4.2 on 2023-05-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab2', '0003_alter_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='model',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
