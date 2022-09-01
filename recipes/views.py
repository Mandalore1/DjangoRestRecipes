from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class TestView(APIView):
    def get(self, request):
        return Response({"Hello": "world"})


class RecipeView(APIView):
    def get(self, request, pk):
        recipe = Recipe.objects.all().select_related("user").prefetch_related("comments__user")
        recipe = get_object_or_404(recipe, pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
