# Generated by Django 2.0 on 2018-06-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0005_auto_20180613_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesfork',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
        migrations.AddField(
            model_name='servicescategories',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
        migrations.AddField(
            model_name='servicessubcategories',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
    ]
