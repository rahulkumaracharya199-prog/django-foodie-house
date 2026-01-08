from django.shortcuts import render
from .models import Category,Product

# Create your views here.


def home(request):

    data = {}
    
    if "cat_id" in request.GET:
        cat_id = request.GET.get("cat_id")
        data["products"] = Product.objects.filter(category=cat_id)

    elif "search" in request.GET:
        search = request.GET.get("search")
        data["products"] = Product.objects.filter(name__contains=search)

    else:
        data["products"] = Product.objects.all()

    data["categories"] = Category.objects.all()

    return render(request, "home.html", data)


def productView(request, product_id):
    data = {}
    data["product"] = Product.objects.get(id=product_id)
    data["categories"] = Category.objects.all()

    return render(request, "productView.html", data)
