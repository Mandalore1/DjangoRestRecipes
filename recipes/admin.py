from django.contrib import admin

from recipes.models import Recipe, Comment, RecipeIngredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(RecipeIngredient)
