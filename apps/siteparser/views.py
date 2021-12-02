import asyncio
import json
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Parser


def index(request):
    rec = Parser.objects.filter(userID=request.user)
    return render(request, "parser.html", {"records": rec})


fname = None


def handler(request):
    if request.user.is_authenticated:
        pass
    if request.method == "POST":
        print(request.POST['site'])
        __request__ = request
        from libs.network import Client
        data = {'site': request.POST['site'], 'patterns': request.POST['patterns'].split(','), 'adaptive': 'False'}
        client = Client('localhost', 9087, handler=responseHeader)
        asyncio.run(client.send(content=data))
        record = Parser(fileName=fname, userID=request.user,
                   patterns=request.POST['patterns'], site=request.POST['site'])
        record.save()
        rec = Parser.objects.filter(userID=request.user)
        print({"message": 'ok', 'records': rec})
        return JsonResponse({"message": 'ok'})
    else:
        return render(request, "index.html", {"data": "error"})


async def responseHeader(**kwargs):
    global fname
    fname = kwargs['content']['data'] + ".json"
    print(fname)