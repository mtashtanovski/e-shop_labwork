from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from webapp.models import Product, Order, OrderProduct
from api_v1.serializers import ProductSerializer, OrderSerializer, OrderedProductSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=204)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class OrderProductViewSet(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderedProductSerializer
    permission_classes = (IsAuthenticated,)

