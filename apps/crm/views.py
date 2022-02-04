from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from datetime import datetime, timedelta

from .lib.crm import getOrders
from .models import CRM


def index(request):
    now = datetime.now()
    prev = now - timedelta(days=31)
    return render(request, "crm.html",
                  {
                      "title": "crm",
                      "error": "ошибка",
                      "months": [now.strftime("%Y-%m"), prev.strftime("%Y-%m")],
                      "projects": [project.name for project in CRM.objects.all()],
                  })


def update(request):
    errorResponse = lambda error: JsonResponse({'data': f'<div id="error">{error}</div>'})

    if request.method == "POST":
        try:
            if ('test' not in request.POST.keys()) and all((request.POST['name'] == '', request.POST['phone'] == '', request.POST['email'] == '')):
                return errorResponse('Для не тестовых заявок хотя бы одно поле (Имя, телефон, email) должно быть заполнено')
            project = CRM.objects.filter(name=request.POST["project"])
            orders = getOrders(
                url=project[0].url if request.POST["branch"] == 'prod' else project[0].url.replace("//", "//dev-"),
                cookie={
                    'PHPSESSID': project[0].prod if request.POST["branch"] == 'prod' else project[0].dev,
                    'mrm': project[0].mrm,
                },
                project=request.POST["project"],
                month=request.POST["month"],
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                manager=project[0].manager if 'test' in request.POST.keys() else "-1"
            )
            if type(orders) is str:
                return errorResponse(orders)
            else:
                return JsonResponse(
                    {
                        'data': loader.render_to_string('crm2.html', {"orders": orders}, request)
                    }
                )
        except Exception as e:
            return errorResponse(e)
    else:
        return errorResponse('Метод только POST')
