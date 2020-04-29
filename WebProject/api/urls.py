from django.urls import path
from .Views.recipe import *
from .Views.user import *
from .Views.category import *
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path(r'recipes/', RecipeList.as_view(), name='RecipeList'),
    path(r'login/', obtain_jwt_token, name='ObtainJWTToken'),
    path(r'signup/', UserCreateAPIView.as_view(), name='Sign-Up'),
    path(r'logout/', logout, name='logout'),
    path(r'categories/', CategoryList.as_view(), name='category-list'),
    path(r'user-list/', UserList.as_view(), name='User-List'),
    path(r'recipes/<str:name>/', RecipeDetail.as_view(), name='RecipeListByName'),
    path(r'categories/<int:category_id>/', category_detail, name='CategoryDetail'),
    path(r'categories/<int:category_id>/recipes/', category_recipes, name='CategoryRecipes'),
    path(r'user/profile/', CurrentUserView.as_view(), name='UserProfile')
]