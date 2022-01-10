from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index_view(request):
    return render(request, 'index.html')
