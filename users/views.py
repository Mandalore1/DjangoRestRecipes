from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from users.serializers import UserDetailSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    """Детальное представление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserListView(ListAPIView):
    """Список пользователей"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
