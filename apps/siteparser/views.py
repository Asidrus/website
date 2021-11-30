import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "parser.html")


def handler(request):
    if request.method == "POST":
        print(request.POST)
        # return HttpResponse(json.dumps({'message': 'ok'}))
        return JsonResponse({"message": 'ok'})
    else:
        return render(request, "index.html", {"data": "error"})