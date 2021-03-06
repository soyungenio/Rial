# Generated by Django 2.0 on 2018-06-13 23:44

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuBullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы')),
                ('content', tinymce.models.HTMLField(default=None, verbose_name='Контент на детальной странице')),
                ('menu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuBullet')),
            ],
            options={
                'verbose_name': 'Страница 1 уровня',
                'verbose_name_plural': 'Страницы 1 уровня',
            },
        ),
        migrations.CreateModel(
            name='Page2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы')),
                ('content', tinymce.models.HTMLField(default=None, verbose_name='Контент на детальной странице')),
                ('menu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuBullet')),
            ],
            options={
                'verbose_name': 'Страница 2 уровня',
                'verbose_name_plural': 'Страницы 2 уровня',
            },
        ),
    ]
