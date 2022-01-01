import asyncio
import json
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import Parser
from libs.network import Client
from .models import Page


def index(request):
    page = Page.objects.filter(id=1)
    print(page)

    return render(request, "documentation.html", {"title": "documentation", "page": page[0].content})