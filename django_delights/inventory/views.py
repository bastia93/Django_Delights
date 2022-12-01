from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem
from .forms import IngredientCreateForm, MenuItemCreateForm, IngredientUpdateForm, MenuItemUpdateForm

# Create your views here.
def home(request):
    return render(request, template_name="inventory/home.html")

# List
class IngredientList(ListView):
    model=Ingredient
    template_name= "inventory/ingredient_list.html"

class MenuItemList(ListView):
    model=MenuItem
    template_name= "inventory/menuitem_list.html"

# Create 
class IngredientCreate(CreateView):
    model=Ingredient
    form_class= IngredientCreateForm
    template_name= "inventory/ingredient_create_form.html"

class MenuItemCreate(CreateView):
    model=MenuItem
    form_class= MenuItemCreateForm
    template_name= "inventory/menuitem_create_form.html"

# Update
class IngredientUpdate(UpdateView):
    model=Ingredient
    form_class= IngredientUpdateForm
    template_name= "inventory/ingredient_update_form.html"

class MenuItemUpdate(UpdateView):
    model=MenuItem
    form_class=MenuItemUpdateForm
    template_name="inventory/menuitem_update_form.html"

# Delete
class IngredientDelete(DeleteView):
    model=Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/inventory/ingredient/list"

class MenuItemDelete(DeleteView):
    model=MenuItem
    template_name="inventory/menuitem_delete_form.html"
    success_url="/inventory/menuitem/list"