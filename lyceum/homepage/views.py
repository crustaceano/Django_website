import http

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    template = 'homepage/home.html'
    context = {}
    return render(request, template, context)


def coffee(request):
    return HttpResponse(
        "<h1>Я чайник</h1>",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
