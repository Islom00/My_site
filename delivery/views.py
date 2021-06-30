from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
    query = request.GET.get("q")
    if query:
        data = Food.objects.filter(Q(name__icontains=query)|Q(category__name__contains=query))
    else:
        data = Food.objects.all()
    context = {
        "objects": data
    }

    return render(request, "delivery/index.html", context)


def view(request, name):
    data = Food.objects.get(name=name)
    context = {
        "object":data
    }

    return render(request, "delivery/view.html", context)


def details(request):
    return render(request, "delivery/details_page.html")


def add(request):
    if request.method == 'POST':

        amount = request.POST.get("amount")
        price = request.POST.get("price")

        result = amount * price

        context = {
            "result": result
        }

        return render(request, "delivery/calculation.html", context)

