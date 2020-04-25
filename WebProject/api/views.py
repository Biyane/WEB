from django.shortcuts import render
from .models import Categories, Recipe
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RecipeSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
# Create your views here.


class RecipeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# @api_view(["GET"])
# def category_recipes(request):
#     recipes = []
#     category = Categories.objects.all()
#     for c in category:
#         for recipe in c:
#             recipes.append(recipe)
#     serializer = RecipeSerializer(recipes, many=True)
#     return Response(serializer.data)


# class CategoriesAPIView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer
