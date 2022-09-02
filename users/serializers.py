from django.contrib.auth.models import User
from rest_framework import serializers


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["id", "password"]