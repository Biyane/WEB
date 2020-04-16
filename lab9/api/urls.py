from django.urls import path
from .views import company_list, company_detail, company_vacancies, vacancies_detail, vacancies_list, vacancies_top_list
urlpatterns = [
    path('companies/', company_list, name='company_list'),
    path('companies/<int:id>', company_detail, name='company_detail'),
    path('companies/<int:id>/vacancies', company_vacancies, name='company_vacancies'),
    path('vacancies/', vacancies_list, name='vacancy_list'),
    path('vacancies/<int:id>', vacancies_detail, name='vacancy_detail'),
    path('vacancies/top_ten', vacancies_top_list, name='top_ten_vacancies'),
]