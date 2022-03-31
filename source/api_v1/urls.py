import pprint
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from api_v1.views import ProductViewSet, OrderViewSet, LogoutView, CartViewSet

app_name = 'api_v1'

eshop_router = routers.DefaultRouter()
eshop_router.register('products', ProductViewSet)
eshop_router.register('orders', OrderViewSet)
eshop_router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(eshop_router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout')
]
