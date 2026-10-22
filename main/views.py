
from django.shortcuts import render
from .models import Product


def index(request):
    products = {
        brand: Product.objects.filter(brand=brand).first()
        for brand in [
            'obertos', 'well', 'djin',
            'puxliykrolik', 'boombubble', 'chokki'
        ]
    }

    return render(request, "main/index.html", {
        "products": products,
    })


def obertos(request):
    return render(request, "main/obertos.html", {
        "products": Product.objects.filter(brand='obertos'),
    })


def well(request):
    return render(request, "main/well.html", {
        "products": Product.objects.filter(brand='well'),
    })


def djin(request):
    return render(request, "main/djin.html", {
        "products": Product.objects.filter(brand='djin'),
    })


def about(request):
    return render(request, "main/about.html")


def puxliykrolik(request):
    return render(request, "main/puxliykrolik.html", {
        "products": Product.objects.filter(brand='puxliykrolik'),
    })


def boombubble(request):
    return render(request, "main/boombubble.html", {
        "products": Product.objects.filter(brand='boombubble'),
    })


def chokki(request):
    return render(request, "main/chokki.html", {
        "products": Product.objects.filter(brand='chokki'),
    })
