from django import forms
from app.models import Products

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", "details", "price", "image", "subCategory", "size"]
