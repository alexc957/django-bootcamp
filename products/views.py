from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Product
# Create your views here.

def home_view(request, *args, **kwargs):

    return HttpResponse("<h1>hello world</h1>")

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
        
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"Product id {obj.id}")
#class HomeView():
 #   pass

def product_api_detail_view(request,pk, *args, **kwargs):
    #obj = Product.objects.get(id=id)
    try:
       
         obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "not found"})

    return JsonResponse({"id": obj.id})