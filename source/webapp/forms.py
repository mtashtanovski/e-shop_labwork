from django import forms
from django.forms import widgets
from webapp.models import CATEGORIES


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label="Наименование товара:")
    description = forms.CharField(max_length=2000, required=False, label="Описание товара:",
                                  widget=widgets.Textarea(attrs={'rows': 7, 'cols': 50}))
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label="Стоимость товара:")
    category = forms.ChoiceField(choices=CATEGORIES, required=True, label="Категория товара:", initial=CATEGORIES[0][1])
    balance = forms.IntegerField(min_value=1, required=True, label="Количество товара:")
