from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def item_list(request):
    template = 'catalog/list.html'
    context = {}
    return render(request, template, context)


def item_detail(request, element):
    return HttpResponse("<body>" + f"Подробно об элементе {element}" + "</body>")
