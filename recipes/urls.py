from django.urls import path

import recipes.views as views

urlpatterns = [
    path('test/', views.TestView.as_view()),
]
