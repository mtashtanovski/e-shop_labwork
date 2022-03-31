from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny, IsAdminUser

from webapp.models import Product, Order, Cart
from api_v1.serializers import ProductSerializer, CartSerializer, OrderSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=204)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

