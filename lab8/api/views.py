from django.shortcuts import render
from api.models import Category, Product
from django.http.response import JsonResponse
from django.http import Http404
# Create your views here.


def category_list(request):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Does not exists")
    return JsonResponse(category.to_json())


def category_products(request, category_i):
    try:
        category = Category.objects.get(id=category_i)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.product_set.all()
    products_json = [p.to_json() for p in products]

    return JsonResponse(products_json, safe=False)


def products(request):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products]
    return JsonResponse(products_json, safe=False)


def products_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("this products does not exists")
    return JsonResponse(product.to_json())
