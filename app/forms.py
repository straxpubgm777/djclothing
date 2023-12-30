from django import forms
from app.models import *

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", "details", "price", "image", "subCategory", "size"]

class BannersForm(forms.ModelForm):
    class Meta:
        model = Banners
        fields = ['image', 'title', 'text']