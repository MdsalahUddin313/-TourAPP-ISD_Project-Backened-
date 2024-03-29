# Generated by Django 3.1.6 on 2021-03-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backened', '0008_auto_20210322_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_name', models.CharField(max_length=120)),
                ('Location_map', models.TextField(default='')),
                ('Location_image', models.TextField(default='')),
                ('Hotels_name_one', models.CharField(max_length=120)),
                ('Hotels_image_one', models.TextField(default='')),
                ('Hotels_name_two', models.CharField(max_length=120)),
                ('Hotels_image_two', models.TextField(default='')),
                ('Hotels_name_three', models.CharField(max_length=120)),
                ('Hotels_image_three', models.TextField(default='')),
                ('location_one', models.CharField(max_length=120)),
                ('location_image_one', models.TextField(default='')),
                ('location_name_two', models.CharField(max_length=120)),
                ('location_image_two', models.TextField(default='')),
                ('location_name_three', models.CharField(max_length=120)),
                ('location_image_three', models.TextField(default='')),
            ],
        ),
    ]
