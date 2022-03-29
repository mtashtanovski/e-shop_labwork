from rest_framework import serializers
from webapp.models import Product, Order, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'balance', 'price')
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'address', 'created_at', 'products')
        read_only_fields = ('id',)


class OrderedProductSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=False)
    product = ProductSerializer(read_only=False)

    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'qty',)
