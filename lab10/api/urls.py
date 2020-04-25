from django.urls import path
from .views import CompanyList, CompanyDetail, company_vacancies,\
    vacancies_detail, vacancies_list, vacancies_top_list
from rest_framework.urlpatterns import format_suffix_patterns
from .auth import UserList, login, logout
from rest_framework_jwt.views import obtain_jwt_token, RefreshJSONWebToken
urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company_list'),
    path('companies/<int:id>', CompanyDetail.as_view(), name='company_detail'),
    path('companies/<int:id>/vacancies', company_vacancies, name='company_vacancies'),
    path('vacancies/', vacancies_list, name='vacancy_list'),
    path('vacancies/<int:id>', vacancies_detail, name='vacancy_detail'),
    path('vacancies/top_ten', vacancies_top_list, name='top_ten_vacancies'),
    path('users/', UserList.as_view(), name='user'),
    path('login/', obtain_jwt_token, name='token_obtain'),
    path('login/refresh/', RefreshJSONWebToken, name='token_refresh'),
    path('logout/', logout),
    # path(r'^api-token-auth/', obtain_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)