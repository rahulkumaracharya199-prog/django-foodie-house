from django.shortcuts import render
from foodie.models import Category, Product

def dashboard(request):
    data = {}
    data["categories"] = Category.objects.all()
    data["products"] = Product.objects.all()
    return render(request, "admin/dashboard.html")


def manageCategory(request):
    data = {}
    data["categories"] = Category.objects.all()

    return render (request, "admin/manageCategory.html", data)


def manageProduct(request):
    data = {}
    data["products"] = Product.objects.all()

    return render (request, "admin/manageProduct.html", data)

