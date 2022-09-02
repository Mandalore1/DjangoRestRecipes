from django.urls import path

import recipes.views as views

urlpatterns = [
    path('test/', views.TestView.as_view(), name="test"),
    path('recipe/', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipe/<int:pk>/', views.RecipeView.as_view(), name="recipe_detail"),
]
