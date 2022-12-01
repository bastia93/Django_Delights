from django import forms
from .models import Ingredient, MenuItem

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model=Ingredient
        fields=("name", "price", "quantity")

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields="__all__"

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model=Ingredient
        fields="__all__"

class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields="__all__"
