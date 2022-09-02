from django.urls import path

import users.views as views

urlpatterns = [
    path("user/<int:pk>/", views.UserDetailView.as_view())
]
