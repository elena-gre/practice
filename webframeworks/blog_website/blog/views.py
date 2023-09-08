from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # type: ignore
    return HttpResponse("Hello, world. You're at the blog index.")


def hello_world(request):  # type: ignore
    return render(request, 'hello_world.html', {})
