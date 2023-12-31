from django.urls import path
from app.views import *

urlpatterns = [
    path("",home_page, name="home_page_url"),
    path("product/<pk>/", product_page,name="product_page_url"),
    path("category/<category>/",categoryPage,name="category_page_url"),
    path("sub_category/<subCategory>/",sub_category_page,name="sub_category_page_url"),
    path('add_product/',add_products,name="add_product_url"),
    path('delet_product/<pk>/', delete_product,name="delete_product_url"),
    path("brands/", brands_page, name="brands_url"),
    path("brands_product/<pk>/", brands_products, name="brands_product_url"),
    path("edit_banner", edit_banner, name="edit_banner_url")
]