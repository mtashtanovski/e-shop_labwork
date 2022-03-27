from django import forms
from django.forms import widgets
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label="Поиск"
    )
