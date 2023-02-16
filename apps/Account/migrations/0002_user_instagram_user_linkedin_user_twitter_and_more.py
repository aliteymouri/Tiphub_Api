# Generated by Django 4.1.3 on 2023-02-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='آدرس اینستاگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='آدرس لینکدین'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='آدرس توییتر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='github',
            field=models.URLField(blank=True, verbose_name='آدرس گیت هاب'),
        ),
    ]
