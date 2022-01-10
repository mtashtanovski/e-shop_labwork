from django.db import models

# Create your models here.
CATEGORIES = [('other', 'Разное'),
              ('laptops', 'Лэптопы'),
              ('gadgets', 'Гаджеты'),
              ('tablets', 'Планшеты'),
              ('cellphones', 'Телефоны')]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=20, default='other', choices=CATEGORIES, verbose_name='Категория')
    balance = models.PositiveIntegerField(default=1, verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')

    def __str__(self):
        return f" {self.pk}. {self.title}, {self.category}: {self.price}, {self.balance}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
