from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

Title = 'это тайтл, Таня!!!'


def index(request):
    return render(request, "index.html", {'user': request.user, 'Title': Title})


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


