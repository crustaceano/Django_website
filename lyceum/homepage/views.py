from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    template = 'homepage/home.html'
    context = {}
    return render(request, template, context)


def cofee(request):
    return HttpResponse(status=418)
