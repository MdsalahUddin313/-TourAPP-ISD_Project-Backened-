# Generated by Django 3.1.5 on 2021-03-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backened', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='hotel_images',
            field=models.TextField(default='no images'),
        ),
    ]