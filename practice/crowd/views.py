from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from .form import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def new(request):
    form = ProductForm()
    return render(request, 'new.html', {'form' : form})

def create(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        new_product = form.save(commit=False)
        new_product.save()
        return redirect('detail', new_product.id)
    return redirect('home')

def detail(request, id):
    # details = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product': product})

def edit(request, id):
    edit_product = Product.objects.get(id=id)
    return render(request, 'edit.html', {'product': edit_product})

def update(request, id):
    update_product = Product.objects.get(id=id)
    update_product.title = request.POST['title']
    update_product.writer = request.POST['writer']
    update_product.description = request.POST['description']
    update_product.expiry_date = request.POST['expiry_date']
    update_product.funding_cost = request.POST['funding_cost']
    update_product.save()
    return redirect('detail', update_product.id)

def delete(request, id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect('home')