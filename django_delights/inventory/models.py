from django.db import models

# Create your models here.

# Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=30, null=False)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def get_absolute_url(self):
        return "/inventory/ingredient/list"

    def __str__(self):
        return self.name
    
# MenuItems
class MenuItem(models.Model):
    name = models.CharField(max_length=30, null=False)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.IntegerField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/inventory/menuitem/list"
