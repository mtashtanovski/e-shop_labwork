from django.db import models

from django.core.validators import MinValueValidator
from django.contrib.sessions.models import Session

# Create your models here.
CATEGORIES = [('other', 'Разное'),
              ('laptops', 'Лэптопы'),
              ('gadgets', 'Гаджеты'),
              ('tablets', 'Планшеты'),
              ('cellphones', 'Телефоны')]


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    category = models.CharField(
        max_length=20,
        default='other',
        choices=CATEGORIES,
        verbose_name='Категория'
    )
    balance = models.PositiveIntegerField(
        default=1,
        verbose_name="Остаток")
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name='Стоимость',
        validators=(MinValueValidator(0),)
    )

    def __str__(self):
        return f"{self.pk}. {self.title} - {self.balance}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='in_cart'
    )
    qty = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1
    )

    def __str__(self):
        return f"{self.product.title} - {self.qty}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Order(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Телефон'
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Адресс'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    products = models.ManyToManyField(
        'webapp.Product',
        related_name='orders',
        verbose_name='Товары',
        through='webapp.OrderProduct',
        through_fields=['order', 'product']
    )

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        verbose_name='Товар',
        related_name='order_products'
    )
    order = models.ForeignKey(
        'webapp.Order',
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        related_name='order_products'
    )
    qty = models.PositiveIntegerField(
        verbose_name='Количество'
    )

    def __str__(self):
        return f'{self.product.title} - {self.order.name} - {self.order.format_time()}'

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
