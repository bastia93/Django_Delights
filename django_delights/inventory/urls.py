from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredients"),
    path("menuitem/list", views.MenuItemList.as_view(), name="menuitems"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("menuitem/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("menuitem/update/<pk>", views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("menuitem/delete/<pk>", views.MenuItemDelete.as_view(), name="menuitemdelete"),
]