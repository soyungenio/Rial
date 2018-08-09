# Generated by Django 2.0 on 2018-06-12 08:30

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_howwedo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Имя')),
                ('job', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Должность')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/block11/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='StuffBullets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(default=None, verbose_name='Пункт')),
                ('stuff', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.Stuff')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/block12/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='ToolsBullets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField(default=None, verbose_name='Пункт')),
                ('stuff', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='about.Tools')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
            },
        ),
        migrations.AlterModelOptions(
            name='howwedo',
            options={'verbose_name': 'Как мы работаем', 'verbose_name_plural': 'Пункт'},
        ),
    ]
