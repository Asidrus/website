import asyncio
import json
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .models import Parser
from libs.network import Client


def index(request):
    return render(request, "documentation.html", {"title": "documentation"})