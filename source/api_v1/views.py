from rest_framework.viewsets import ModelViewSet

from webapp.models import Product, Order, OrderProduct
from api_v1.serializers import ProductSerializer, OrderSerializer, OrderedProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProductViewSet(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderedProductSerializer
