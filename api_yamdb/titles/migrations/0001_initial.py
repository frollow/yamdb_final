# Generated by Django 2.2.16 on 2021-11-13 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории', max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Slug для категории', unique=True, verbose_name='Slug для категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название жанра', max_length=256, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Slug для жанра', unique=True, verbose_name='Slug для жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название произведения', max_length=256, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(help_text='Год издания', verbose_name='Год')),
                ('description', models.TextField(help_text='Описание', verbose_name='Описание')),
                ('rating', models.PositiveSmallIntegerField(blank=True, default=None, help_text='Рейтинг произведения', null=True, verbose_name='Оценка')),
                ('category', models.ForeignKey(help_text='Название Категории', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='titles.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(help_text='Жанр', related_name='titles', to='titles.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ['id'],
            },
        ),
    ]
