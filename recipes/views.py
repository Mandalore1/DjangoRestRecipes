from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.serializers import *


class TestView(APIView):
    def get(self, request):
        return Response({"Hello": "world"})


class RecipeView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all().select_related("user").prefetch_related("comments__user")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeDetailSerializer
        elif self.request.method in ("PUT", "PATCH"):
            return RecipeUpdateSerializer

    # def get(self, request, pk):
    #     recipe = Recipe.objects.all().select_related("user").prefetch_related("comments__user")
    #     recipe = get_object_or_404(recipe, pk=pk)
    #     serializer = RecipeDetailSerializer(recipe)
    #     return Response(serializer.data)


class RecipeListView(ListCreateAPIView):
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeListSerializer
        elif self.request.method == "POST":
            return RecipeCreateSerializer

    # def get(self, request):
    #     recipes = Recipe.objects.all()
    #     serializer = RecipeListSerializer(recipes, many=True)
    #     return Response(serializer.data)
