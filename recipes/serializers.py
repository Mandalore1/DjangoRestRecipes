from django.contrib.auth.models import User
from rest_framework import serializers

from recipes.models import Recipe, Comment, RecipeIngredient


class UserNameSerializer(serializers.ModelSerializer):
    """Берет только имя пользователя у пользователя"""
    class Meta:
        model = User
        fields = ["username"]


class CommentSerializer(serializers.ModelSerializer):
    """Комментарий"""
    user = UserNameSerializer()

    class Meta:
        model = Comment
        exclude = ["id"]


class RecipeIngredientSerializer(serializers.ModelSerializer):
    """Ингредиент рецепта"""
    class Meta:
        model = RecipeIngredient
        exclude = ["id", "recipe"]


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Детальное представление рецепта"""
    user = UserNameSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    ingredients = RecipeIngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        exclude = ["id", "favorited_by"]


class RecipeListSerializer(serializers.ModelSerializer):
    """Сокращенное представление рецепта"""
    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "created_at", "image"]


class RecipeCreateSerializer(serializers.ModelSerializer):
    """Сериализатор начального создания рецепта"""
    class Meta:
        model = Recipe
        fields = ["title", "description"]

    def create(self, validated_data):
        """Создание рецепта"""
        # Устанавливаем пользователем рецепта текущего пользователя
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class RecipeUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления рецепта"""
    class Meta:
        model = Recipe
        fields = ["title", "description", "content", "image", "is_published"]
