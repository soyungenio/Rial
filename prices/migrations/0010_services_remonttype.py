# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-22 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0009_pricesfork_calcprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='remonttype',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='prices.PricesFork', verbose_name='Тип ремонта'),
        ),
    ]
