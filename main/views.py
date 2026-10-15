
from django.shortcuts import render
from .models import Product


def index(request):
    products = {
        brand: Product.objects.filter(brand=brand).first()
        for brand in ['obertos', 'well', 'djin']
    }

    return render(request, "main/index.html", {
        "products": products,
    })


def obertos(request):
    return render(request, "main/obertos.html")


def well(request):
    return render(request, "main/well.html")


def djin(request):
    return render(request, "main/djin.html")


def about(request):
    return render(request, "main/about.html")
