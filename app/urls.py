from django.urls import path
from app.views import *

urlpatterns = [
    path("",home_page, name="home_page_url"),
    path("product/<pk>/", product_page,name="product_page_url"),
    path("category/<category>/",categoryPage,name="category_page_url"),
    path("sub_category/<subCategory>/",sub_category_page,name="sub_category_page_url"),
]