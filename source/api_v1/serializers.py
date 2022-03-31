from rest_framework import serializers
from webapp.models import Product, Order, OrderProduct, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


class OrderedProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = OrderedProductSerializer(read_only=True, many=True, source='order_products')

    class Meta:
        model = Order
        fields = ['id', 'name', 'address', 'phone', 'products', 'created_at']
