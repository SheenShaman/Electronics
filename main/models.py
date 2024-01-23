from django.utils import timezone

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Link(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    product = models.ManyToManyField('Product', verbose_name='Продукт')

    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    def __str__(self):
        return f'{self.title} ({self.email}, {self.country}, {self.city}, {self.street}, {self.house_number})'

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'


class Product(models.Model):
    product_title = models.CharField(max_length=50, verbose_name='Название продукта')
    product_launch_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.product_title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
