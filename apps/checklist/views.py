from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import categorys, params, blocks, itemName, pages


def index(request):

    category = categorys.objects.all()
    param = params.objects.all()
    block = blocks.objects.all()
    points = itemName.objects.all()
    sub_items = pages.objects.all()
    return render(request, "web-developer-checklist.html",
    context={
        'category_bloks': category,
        'blocks': block,
        'points': points,
        'param': param,
        'sub_items': sub_items,
    })

# Create your views here.
