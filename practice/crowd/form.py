
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'writer', 'description', 'target_price', 'expiry_date', 'funding_cost']