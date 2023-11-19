from django.shortcuts import render,get_object_or_404
from app.models import *
from bs4 import BeautifulSoup
import requests
from django.core.files import File
from io import BytesIO

def home_page(request):
    products = Products.objects.all()
    more_images = MoreImages.objects.all()
    return render(request, "home.html",{
        "products":products,
        "more_images":more_images
    })

def product_page(request,pk):
    product = Products.objects.get(pk=pk)
    more_images = MoreImages.objects.filter(product=pk)
    return render(request,"product_page.html",{
        "product":product,
        "more_images":more_images
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

