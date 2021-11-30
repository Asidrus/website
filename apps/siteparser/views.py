from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "parser.html")


def handler(request):
    print(request.POST)
    return HttpResponse("ok")