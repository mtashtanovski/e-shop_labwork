from django.urls import path

from webapp.views import (
    IndexView,
    ProductView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CartAddView,
    CartView,
    CartDeleteView,
    CartDeleteOneView,
    OrderCreateView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/add-to-cart/', CartAddView.as_view(), name='product_add_to_cart'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete_view'),
    path('cart/<int:pk>/delete-one/', CartDeleteOneView.as_view(), name='cart_delete_one_view'),
    path('order/create/', OrderCreateView.as_view(), name='order_create_view'),
]
