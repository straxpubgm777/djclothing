from django.shortcuts import render,get_object_or_404, redirect
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import user_passes_test
from bs4 import BeautifulSoup
import requests

def home_page(request):
    products = Products.objects.all()
    more_images = MoreImages.objects.all()
    return render(request, "home.html",{
        "products":products,
        "more_images":more_images
    })

def product_page(request,pk):
    product = Products.objects.get(pk=pk)
    products = Products.objects.filter(subCategory=product.subCategory)
    more_images = MoreImages.objects.filter(product=pk)
    return render(request,"product_page.html",{
        "product":product,
        "more_images":more_images,
        "products":products
    })

def categoryPage(request, category):
    category_instance = get_object_or_404(Category, pk=category)
    subcategories = SubCategory.objects.filter(category=category_instance)
    products = Products.objects.filter(subCategory__in=subcategories)
    

    return render(request, "category.html", {
        "products": products,
        "category_instance":category_instance
    })

def sub_category_page(request ,subCategory):
    sub_products = Products.objects.filter(subCategory=subCategory)
    return render(request, "sub_category.html",{
        "sub_products":sub_products
    })

def add_products(request):
    error = ""
    form = AddProductsForm()

    if request.method == 'POST':
        form = AddProductsForm(request.POST, request.FILES)  # Include request.FILES for handling uploaded files
        if form.is_valid():
            if 'image' in form.cleaned_data and form.cleaned_data['image'] is None:
                form.cleaned_data['image'] = None

            form.save()
            return redirect('app:home_page_url')
        else:
            error = "Please correct the errors below."

    return render(request, 'add_products.html', {
        'form': form,
        "error": error
    })
add_products = user_passes_test(lambda u: u.is_authenticated and u.is_staff)(add_products)


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect("app:home_page_url")

def brands_page(request):
    brands = Brands.objects.all()
    return render(request, "brands.html",{"brands":brands})

def brands_products(request, pk):
    brands = Brands.objects.get(pk=pk)
    return render(request, "brands_product.html", {
        'brands':brands
    })