from django.urls import path

import users.views as views

urlpatterns = [
    path("user/", views.UserListView.as_view(), name="user_list"),
    path("user/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
]
