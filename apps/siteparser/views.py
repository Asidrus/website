import asyncio
import json
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Parser
from libs.network import Client


def index(request):
    rec = Parser.objects.filter(userID=request.user)
    return render(request, "parser.html", {"records": rec})


fname = None


def handler(request):
    if request.user.is_authenticated:
        pass
    if request.method == "POST":
        try:
            print(request.POST)
            data = {'site': request.POST['site'], 'patterns': request.POST['patterns'].split(','), 'adaptive': 'False'}
            client = Client('localhost', 9087, handler=responseHeader)
            asyncio.run(client.send(content=data))
            record = Parser(fileName=fname, userID=request.user,
                       patterns=request.POST['patterns'], site=request.POST['site'])
            record.save()
            return JsonResponse(
                {"message": f' будет доступен по <a href="/media/{fname}" target="_blank">ссылке</a> через 3-5 минут'})
        except Exception as e:
            return JsonResponse({"data": "e"})
    else:
        return JsonResponse({"data": "error"})


async def responseHeader(**kwargs):
    global fname
    fname = kwargs['content']['data'] + ".json"