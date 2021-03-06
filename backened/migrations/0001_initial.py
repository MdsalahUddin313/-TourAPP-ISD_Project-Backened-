# Generated by Django 3.1.5 on 2021-02-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=150)),
                ('createdAt', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subcategory', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=150)),
                ('city_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=150)),
                ('country_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='transports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_company_name', models.CharField(max_length=150)),
                ('transport_code', models.CharField(max_length=15)),
                ('transport_address', models.CharField(max_length=250)),
                ('company_type_id', models.IntegerField(max_length=200)),
                ('transport_details', models.TextField()),
                ('is_partner', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backened.city')),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=150)),
                ('hotel_code', models.CharField(max_length=15)),
                ('hotel_address', models.CharField(max_length=250)),
                ('hotel_details', models.TextField()),
                ('is_partner', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backened.city')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backened.country'),
        ),
        migrations.CreateModel(
            name='Articles_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('metatitle', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('publishedAt', models.DateTimeField()),
                ('content', models.TextField()),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backened.authors')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backened.category')),
            ],
        ),
    ]
