import pprint

from rest_framework import serializers
from webapp.models import Product, Order, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'category', 'balance', 'price')
        read_only_fields = ('id',)


class OrderedProductSerializer(serializers.ModelSerializer):
    # order = serializers.PrimaryKeyRelatedField(read_only=True)
    # product = serializers.PrimaryKeyRelatedField(read_only=True)
    # product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'qty')


class OrderSerializer(serializers.ModelSerializer):
    # products = OrderedProductSerializer(many=True)
    # products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'name', 'phone', 'address', 'created_at', 'products')

