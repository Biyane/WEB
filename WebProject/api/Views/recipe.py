from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Recipe
from api.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    #CBV
# class RecipeListAPIView(APIView):
#     def get(self, request):
#         recipies = Recipe.objects.all()
#         serializer = RecipeSerializer(recipies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#CBV
class RecipeDetailAPIView(APIView):

    def get_object(self, recipe_id):
        try:
            return Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, recipe_id):
        recipe = self.get_object(recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, recipe_id):
        recipe = self.get_object(recipe_id)
        serializer = RecipeSerializer(instance=recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})

    def delete(self, request, recipe_id):
        recipe = self.get_object(recipe_id)
        recipe.delete()

        return Response({'deleted': True})


#CBV
class RecipeByCategoryAPIView(APIView):
    def get(self, request, category_id):
        recipes = Recipe.objects.filter(category=category_id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)