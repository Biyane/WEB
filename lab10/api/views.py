from django.shortcuts import render
from .models import Company, Vacancy
from django.http import JsonResponse, HttpResponse, Http404
from .serializers import CompanySerializer, CompanySerializer2, VacancySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         companies_json = [c.to_json() for c in companies]
#         return JsonResponse(companies_json, safe=False)
#     elif request == 'POST':
#         pass

# @csrf_exempt
# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         # 1 option
#         # data = json.loads(request.body)
#         # 2 option
#         data = JSONParser().parse(request)
#         serializer = CompanySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# class CompanyList(APIView):
#     def get(self, request, format=None):
#         company = Company.objects.all()
#         serializer = CompanySerializer2(company, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, statis=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def company_detail(request, id):
#     try:
#         company = Company.objects.get(pk=id)
#     except Company.DoesNotExist:
#         raise Http404("no company exists")
#     if request.method == 'GET':
#         serializer = CompanySerializer(company)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = CompanySerializer(company, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         company.delete()
#         return HttpResponse(status=200)

# class CompanyDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Company.objects.get(pk=id)
#         except Company.DoesNotExist:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         company = self.get_object(id)
#         serializer = CompanySerializer2(company)
#         return Response(serializer.data)
#
#     def put(self, request, id, format=None):
#         company = self.get_object(id)
#         serializer = CompanySerializer2(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id, format=None):
#         company = self.get_object(id)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# def company_vacancies(request, id):
#     try:
#         company = Company.objects.get(pk=id)
#     except Company.DoesNotExist:
#         raise Http404("no vacancies exists")
#     vacancies = company.vacancy_set.all()
#     vacancies_json = [v.to_json() for v in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
@api_view(['GET', 'POST'])
def company_vacancies(request, id):
    # try:
    #     comp_vacancies = Company.objects.get(pk = id)
    # except Company.DoesNotExist:
    #     raise Http404("no company exists")
    if request.method == 'GET':
        comp_vacancies = Company.objects.get(pk=id)
        vacancies = comp_vacancies.vacancy_set.all()
        serializer = CompanySerializer2(vacancies, many=True)
        return Response(serializer.data)

# def vacancies_list(request):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [v.to_json() for v in vacancies]
#     return JsonResponse(vacancies_json, safe=False)


@api_view(['GET', 'POST'])
def vacancies_list(request, format=None):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def vacancies_detail(request, id):
#     try:
#         vacancy = Vacancy.objects.get(pk=id)
#     except Company.DoesNotExist:
#         raise Http404("no vacancy exists")
#     if request.method == 'PUT':
#         request_body = JSONParser().parse(request)
#         vacancy.name = request_body.get('name', vacancy.name)
#         vacancy.description = request_body.get('description', vacancy.description)
#         vacancy.company = request_body.get('company', vacancy.company)
#         vacancy.salary = request_body.get('salary', vacancy.salary)
#         vacancy.save()
#         return JsonResponse(vacancy.to_json())
#     return JsonResponse(vacancy.to_json())


@api_view(['GET', 'PUT'])
def vacancies_detail(request, id, format=None):
    try:
        vacancy = Vacancy.objects.get(pk=id)
    except Vacancy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(VacancySerializer(vacancy).data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def vacancies_top_list(request):
    if request.method == 'GET':
        # vacancy_array = [Vacancy(
        #     name="kema" + str(i), description="kema",salary= i + 1, company=Company.objects.get(pk=1)
        # ) for i in range(10)]
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        # vacancies_json = [v.to_json() for v in vacancies]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        # vacancy = Vacancy.objects.filter(salary__gte=15).order_by('-salary')
        # vacancy = Vacancy.objects.get(pk=1)
        # return JsonResponse(vacancy.array_json(), safe=False)
        # pass
        raise Http404("this is not GET request")


# class CompanyList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer2
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class CompanyDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer2
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class CompanyList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        return CompanySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    # queryset = Company.objects.all()
    # serializer_class = CompanySerializer2


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


