from django.urls import path

from webapp.views import (
    IndexView,
    ProductView,
    ProductCreateView,
    ProductUpdateView,
    DeleteProductView,
)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product')
]
