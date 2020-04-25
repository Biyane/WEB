from django.urls import path
from .views import RecipeList, UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path(r'recipe/', RecipeList.as_view(), name='RecipeList'),
    path(r'login/', obtain_jwt_token, name='ObtainJWTToken'),
    path(r'signup/', UserCreateAPIView.as_view(), name='Sign-Up'),
    # path(r'categoryR', category_recipes, name='Рецепты Категория'),
]