from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView

from users.serializers import UserDetailSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
