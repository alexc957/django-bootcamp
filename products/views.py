from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from .models import Product
# Create your views here.
from .forms import ProductForm
#def bad_view(request,*args,**kwargs):
    #print(request.GET)
    #my_request_data = dict(request.GET)
    #new_product = my_request_data.get("new_product")
    #if new_product[0].lower() == "true":
        #print("true")
        #Product.objects.create(
       ##     title = my_request_data.get("title")[0],
      #      content=my_request_data.get("content")[0],

     #   )
    #return HttpResponse("dont do this")
#def product_create_view(request, *args, **kwargs):
#    print(request.POST)
#    print(request.GET) 
 #   if request.method == "POST":
  #      post_data = request.POST or None
   #     if post_data != None:
    #        my_form = ProductForm(request.POST)
     #       print(my_form.is_valid())
      #      if my_form.is_valid():
       #         print(my_form.cleaned_data.get("title"))
        #        title_from_input =my_form.cleaned_data.get("title")
         #       Product.objects.create(title=title_from_input)
          #  print(post_data)
    #return render(request, "forms.html",{})
def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        #print(form.cleaned_data)
        #Product.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.save()
        form = ProductForm()
    return render(request, "forms.html",{"form": form})

def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])    
        #return HttpResponse("<h1>hello world</h1>")
    print(qs)
    context = {"name":"Alex"}
    return render(request, "home.html",context) # 

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(id=pk)
        
    except Product.DoesNotExist:
        raise Http404
    #return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/detail.html", {"object": obj})
#class HomeView():
 #   pass

def product_api_detail_view(request,pk, *args, **kwargs):
    #obj = Product.objects.get(id=id)
    try:
       
         obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "not found"})

    return JsonResponse({"id": obj.id})



def product_list_view(request,*args,**kwargs):
    qs = Product.objects.all()
    context = {"object_list":qs }

    return render(request,"products/list.html",context)