from django import forms
from webapp.models import Product, Cart, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=30,
        label='Найти',
        widget=forms.TextInput(
            attrs={'class': 'myfieldclass'}
        )
    )


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['qty']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['products']
