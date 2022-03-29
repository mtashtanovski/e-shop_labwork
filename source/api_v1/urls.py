import pprint
from rest_framework import routers
from django.urls import path, include
from api_v1.views import ProductViewSet, OrderViewSet, OrderProductViewSet

app_name = 'api_v1'

eshop_router = routers.DefaultRouter()
eshop_router.register('products', ProductViewSet)
eshop_router.register('orders', OrderViewSet)
eshop_router.register('order-product', OrderProductViewSet)

pprint.pprint(eshop_router.urls)

urlpatterns = [
    path('', include(eshop_router.urls),)
]
