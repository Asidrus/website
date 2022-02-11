from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import categorys, blocks, itemName, pages


def index(request):

    category = categorys.objects.all()
    items = blocks.objects.all()
    points = itemName.objects.all()
    sub_items = pages.objects.all()
    return render(request, "web-developer-checklist.html",
    context={
        'category_bloks': category,
        'items': items,
        'points': points,
        'sub_items0': sub_items
    })

# Create your views here.
