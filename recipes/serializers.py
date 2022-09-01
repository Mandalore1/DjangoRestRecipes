from django.contrib.auth.models import User
from rest_framework import serializers

from recipes.models import Recipe, Comment


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CommentSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()

    class Meta:
        model = Comment
        exclude = ["id"]


class RecipeSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        exclude = ["id", "favorited_by"]
