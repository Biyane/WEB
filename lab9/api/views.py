from django.shortcuts import render
from .models import Company, Vacancy
from django.http.response import JsonResponse
from django.http import Http404


# Create your views here.


def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    elif request == 'POST':
        pass


def company_detail(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        raise Http404("no company exists")
    return JsonResponse(company.to_json())


def company_vacancies(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        raise Http404("no vacancies exists")
    vacancies = company.vacancy_set.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancies_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Company.DoesNotExist:
        raise Http404("no vacancy exists")
    return JsonResponse(vacancy.to_json())


def vacancies_top_list(request):
    if request.method == 'GET':
        # vacancy_array = [Vacancy(
        #     name="kema" + str(i), description="kema",salary= i + 1, company=Company.objects.get(pk=1)
        # ) for i in range(10)]
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    else:
        # vacancy = Vacancy.objects.filter(salary__gte=15).order_by('-salary')
        # vacancy = Vacancy.objects.get(pk=1)
        # return JsonResponse(vacancy.array_json(), safe=False)
        # pass
        raise Http404("this is not GET request")
