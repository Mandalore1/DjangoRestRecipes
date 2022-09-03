from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from users.permissions import SameUserOrReadOnly
from users.serializers import UserDetailSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    """Детальное представление пользователя"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [SameUserOrReadOnly]


class UserListView(ListAPIView):
    """Список пользователей"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
