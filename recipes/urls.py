from django.urls import path

import recipes.views as views

urlpatterns = [
    path('test/', views.TestView.as_view()),
    path('recipe/<int:pk>/', views.RecipeView.as_view())
]
