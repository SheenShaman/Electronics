from django.utils import timezone

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Contacts(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название компании')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Link(models.Model):
    NAMES = (
        ('Factory', 'Factory'),
        ('Retail', 'Retail network'),
        ('Trader', 'Sole trader')
    )

    name = models.CharField(max_length=50, choices=NAMES, verbose_name='Название звена сети')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    product = models.ManyToManyField('Product', verbose_name='Продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'


class Product(models.Model):
    product_title = models.CharField(max_length=50, verbose_name='Название продукта')
    model = models.CharField(max_length=50, verbose_name='Модель продукта')
    product_launch_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.product_title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
