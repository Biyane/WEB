from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.serializers import CategorySerializer, RecipeSerializer
from api.models import Categories


@permission_classes([permissions.IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def category_detail(request, category_id):
    try:
        category = Categories.objects.get(id=category_id)
    except Categories.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(serializer.instance, request.data)
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def category_recipes(request, category_id):
    try:
        category = Categories.objects.get(pk=category_id)
    except Categories.DoesNotExist as e:
        return Response({'error': str(e)})

    cat_recipes = category.recipe_set.all()
    recipes = RecipeSerializer(cat_recipes, many=True)
    return Response(recipes.data, status=status.HTTP_200_OK)
