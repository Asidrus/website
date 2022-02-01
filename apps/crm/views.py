from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

import requests


def index(request):
    # page = Page.objects.filter(id=1)
    # print(page)

    orders = [
        {
            "name": "Антон",
            "email": "tester_form@gaps.edu.ru",
            "phone": "81234567890",
            "datetime": "2022-02-01 09:24:20",
            "project": "adpo",
            "product": "Младший фармацевт (340ч)"
        },
        {
            "name": "Антон",
            "email": "tester_form@gaps.edu.ru",
            "phone": "81234567890",
            "datetime": "2022-02-01 09:24:20",
            "project": "adpo",
            "product": "Младший фармацевт (340ч)"
        }
    ]

    return render(request, "crm.html",
                  {
                      "title": "crm",
                      "error": "ошибка",
                      "months": ["02.2022", "03.2022"],
                      "projects": ["penta", "mult", "psy"],
                      "orders": orders
                  })


def update(request):
    if request.method == "POST":
        try:
            print(request.POST)
            # data = {'site': request.POST['site'], 'patterns': request.POST['patterns'].split(','), 'adaptive': 'False'}

            return JsonResponse()
        except Exception as e:
            return JsonResponse({"data": "e"})
    else:
        return JsonResponse({"data": "error"})