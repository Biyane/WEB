from django.shortcuts import render
from .models import Company, Vacancy
from django.http import JsonResponse, HttpResponse
from django.http import Http404
from .serializers import CompanySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

# Create your views here.


# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         companies_json = [c.to_json() for c in companies]
#         return JsonResponse(companies_json, safe=False)
#     elif request == 'POST':
#         pass

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # 1 option
        # data = json.loads(request.body)
        # 2 option
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        raise Http404("no company exists")
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=200)


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
    if request.method == 'PUT':
        request_body = JSONParser().parse(request)
        vacancy.name = request_body.get('name', vacancy.name)
        vacancy.description = request_body.get('description', vacancy.description)
        vacancy.company = request_body.get('company', vacancy.company)
        vacancy.salary = request_body.get('salary', vacancy.salary)
        vacancy.save()
        return JsonResponse(vacancy.to_json())
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
