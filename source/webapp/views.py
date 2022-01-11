from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.models import Product
from webapp.forms import ProductForm


def index_view(request):
    products = Product.objects.order_by('category', '-title')
    return render(request, 'index.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'product': product})


def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            category = form.cleaned_data.get('category')
            balance = form.cleaned_data.get('balance')
            new_product = Product.objects.create(title=title, description=description,
                                                 price=price, category=category, balance=balance)
            return redirect('index')
        return render(request, 'add_product.html', {"form": form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'balance': product.balance
        })
        return render(request, 'update_product.html', {'product': product, 'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = request.POST.get('title')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.category = request.POST.get('category')
            product.balance = request.POST.get('balance')
            product.save()
            return redirect('index')
        return render(request, 'update_product.html', {'product': product, 'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_product.html', {'product': product})
    else:
        product.delete()
        return redirect('index')
