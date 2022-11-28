# Generated by Django 4.1.3 on 2022-11-11 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی مرجع ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد در ')),
            ],
            options={
                'verbose_name': 'دسته بندی مرجع',
                'verbose_name_plural': 'دسته بندی های مرجع ',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='عنوان دسته بندی ')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت ')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='آدرس اسلاگ ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد در ')),
                ('category', models.ManyToManyField(related_name='subcategories', to='Video.category', verbose_name='زیرمجموعه دسته بندی ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان ویدیو')),
                ('video', models.FileField(upload_to='videos/', verbose_name='آپلود ویدیو')),
                ('about_video', models.TextField(verbose_name='درباره ویدئو')),
                ('video_cover', models.ImageField(upload_to='banner', verbose_name='بنر ویدیو')),
                ('video_time', models.CharField(blank=True, max_length=15, null=True, verbose_name='تایم ویدیو')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت ')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='آدرس اسلاگ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار در ')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی در ')),
                ('category', models.ManyToManyField(related_name='videos', to='Video.subcategory', verbose_name='دسته بندی ویدیو')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='منتشر کننده')),
            ],
            options={
                'verbose_name': 'ویدیو',
                'verbose_name_plural': 'ویدیوها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(verbose_name='متن کامنت ')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت در ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Video.comment', verbose_name='زیرمجموعه')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Video.video', verbose_name='ویدیو')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
                'ordering': ('-created_at',),
            },
        ),
    ]