from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {'user': False})
    else:
        return render(request, "index.html", {'user': True})
    # return HttpResponse("hello world")


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


