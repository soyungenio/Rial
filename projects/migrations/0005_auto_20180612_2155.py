# Generated by Django 2.0 on 2018-06-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180612_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimages',
            options={'ordering': ['-is_main'], 'verbose_name': 'Фото проекта', 'verbose_name_plural': 'Фото проектов'},
        ),
        migrations.AddField(
            model_name='projects',
            name='design',
            field=models.BooleanField(default=False, verbose_name='Дизайн проект'),
        ),
    ]
