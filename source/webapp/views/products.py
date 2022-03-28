from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.models import Product
from webapp.forms import ProductForm
from webapp.views.base_views import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'title']
    search_fields = ['title__icontains']
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(balance__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = "webapp:product_update"
        context['product_pk'] = self.get_object().pk
        return context

    def get_queryset(self):
        return super().get_queryset().filter(balance__gt=0)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_product.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('webapp:index')
