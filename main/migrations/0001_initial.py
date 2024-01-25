# Generated by Django 4.2 on 2024-01-25 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=50, verbose_name='Модель продукта')),
                ('product_launch_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название компании')),
                ('network_object', models.CharField(choices=[('0', 'Factory'), ('1', 'Retail network'), ('2', 'Sole trader')], max_length=50, verbose_name='Объект сети')),
                ('debt', models.FloatField(blank=True, null=True, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.contacts', verbose_name='Контакты')),
                ('product', models.ManyToManyField(to='main.product', verbose_name='Продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.link', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
