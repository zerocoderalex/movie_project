# Generated by Django 5.1.3 on 2024-11-30 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]
