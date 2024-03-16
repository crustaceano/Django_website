from django.http import HttpResponse
from django.shortcuts import render

import catalog.models


# Create your views here.
def item_list(request):
    template = 'catalog/list.html'
    # items = catalog.models.Item.objects.only('name', 'text', 'category', 'id')
    items = catalog.models.Item.objects.select_related('category').only('name', 'text', 'id', 'category__name')
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request, element):
    return HttpResponse("<body>" + f"Подробно об элементе {element}" + "</body>")
