from django.urls import path

from webapp.views import (
    index_view,
    product_view,
    add_product,
    update_product,
    delete_product
)

urlpatterns = [
    path('', index_view, name='index'),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('product/add/', add_product, name='add_product'),
    path('product/<int:pk>/update/', update_product, name='update_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product')
]