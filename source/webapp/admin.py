from django.contrib import admin
from webapp.models import Product, OrderProduct, Cart, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'balance', 'price']
    list_display_links = ['id', 'title']
    list_filter = ['category']
    search_fields = ['title']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    fields = ('product', 'qty')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'created_at')
    list_display_links = ('pk', 'name')
    ordering = ["-created_at"]
    inlines = (OrderProductInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
