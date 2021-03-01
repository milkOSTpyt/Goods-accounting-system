from django.db import models


class Shop(models.Model):
    """Магазин"""
    name = models.CharField(max_length=125, verbose_name='Название')
    domain = models.CharField(max_length=125, verbose_name='Домен')
    link = models.URLField(max_length=155, verbose_name='Адрес')

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Warehouse(models.Model):
    """Склад"""
    name = models.CharField(max_length=75, verbose_name='Название склада')
    shop = models.ManyToManyField(Shop, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Category(models.Model):
    """Модель категорий"""
    title = models.CharField(max_length=150, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Товар"""
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена')
    sold_out = models.BooleanField(default=False, verbose_name='Продан ли')
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория',
                                 related_name='category')
    warehouse = models.ForeignKey(Warehouse,
                                  on_delete=models.CASCADE,
                                  verbose_name='Склад',
                                  related_name='warehouse')
    shop = models.ForeignKey(Shop,
                             on_delete=models.CASCADE,
                             verbose_name='Магазин',
                             related_name='shop')

    def __str__(self):
        return f'{self.name} -> {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['price']
