# Generated by Django 4.1.3 on 2023-02-08 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20, verbose_name='نام و نام خانوادگی')),
                ('skill', models.CharField(max_length=30, verbose_name='مهارت')),
                ('email', models.EmailField(max_length=254, verbose_name='آدرس ایمیل')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('resume', models.FileField(upload_to='resume', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='رزومه')),
            ],
            options={
                'verbose_name': 'درخواست تدریس',
                'verbose_name_plural': 'درخواست\u200cهای تدریس',
            },
        ),
    ]
