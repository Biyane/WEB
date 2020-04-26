from django.urls import path
from .Views.recipe import RecipeList
from .Views.user import UserCreateAPIView, logout, Logout
from .Views.category import category_list
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path(r'recipe/', RecipeList.as_view(), name='RecipeList'),
    path(r'login/', obtain_jwt_token, name='ObtainJWTToken'),
    path(r'signup/', UserCreateAPIView.as_view(), name='Sign-Up'),
    path(r'logout/', Logout.as_view(), name='logout'),
    path(r'categories/', category_list, name='category-list')
]