from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# from .models import Example

def index(request):
    # res = Example.objects.filter(id=2)
    # return render(request, "web-developer-checklist.html", {"Title": "Приложуха Тани"})
    return render(request, "web-developer-checklist.html")

# Create your views here.
