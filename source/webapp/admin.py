from django.contrib import admin
from webapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class GuestAdmin(admin.ModelAdmin):
        list_display = ['id', 'title', 'category', 'balance', 'price']
        list_filter = ['category', 'title']
        search_fields = ['title']
        fields = [
            'title',
            'category',
            'balance',
            'price',
            'description',
        ]
        readonly_fields = []


admin.site.register(Product, ProductAdmin)
