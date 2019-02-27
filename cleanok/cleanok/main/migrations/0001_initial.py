# Generated by Django 2.1.5 on 2019-02-27 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_name', models.CharField(max_length=20, unique=True, verbose_name='Достоинство')),
                ('info_description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Пункт информации',
                'verbose_name_plural': 'Пукнты информации',
            },
        ),
        migrations.CreateModel(
            name='OrderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=20, verbose_name='Эл. почта')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('review_text', models.TextField(verbose_name='Отзыв')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата написания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Наименование')),
                ('short_desc', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServiceWorksNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=50, verbose_name='Наименование работы')),
                ('min_price', models.SmallIntegerField(verbose_name='Минимальная цена')),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Service')),
            ],
            options={
                'verbose_name': 'Наименование работы',
                'verbose_name_plural': 'Наименование работ',
            },
        ),
        migrations.CreateModel(
            name='ShortInfoAboutCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_about', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Краткая информация о компании',
                'verbose_name_plural': 'Краткая информация о компании',
            },
        ),
        migrations.CreateModel(
            name='SpecialService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Наименование')),
                ('short_desc', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Спец. Услуга',
                'verbose_name_plural': 'Спец. Услуги',
            },
        ),
        migrations.CreateModel(
            name='SpecialServiceWorksNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=50, verbose_name='Наименование работы')),
                ('input_choice', models.CharField(choices=[('Цена, колич-во и ед. измерения', 'Цена, колич-во и ед. измерения'), ('Текст', 'Текст')], default='Цена, колич-во и ед. измерения', max_length=30, verbose_name='Тип ячейки')),
                ('min_price', models.SmallIntegerField(blank=True, null=True, verbose_name='Минимальная цена')),
                ('count', models.SmallIntegerField(blank=True, null=True, verbose_name='Количество')),
                ('units', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ед. измерения')),
                ('alternate_text', models.TextField(blank=True, null=True, verbose_name='Альтернативный текст')),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SpecialService', to_field='name')),
            ],
            options={
                'verbose_name': 'Наименование спец. работы',
                'verbose_name_plural': 'Наименование спец. работ',
            },
        ),
        migrations.CreateModel(
            name='WhyWe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название элемента')),
                ('description', models.TextField(verbose_name='Описание элемента')),
            ],
            options={
                'verbose_name': 'Почему мы',
                'verbose_name_plural': 'Почему мы',
            },
        ),
    ]
