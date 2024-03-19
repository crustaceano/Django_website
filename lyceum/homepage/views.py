import http

from django.shortcuts import render
from django.http import HttpResponse
import catalog.models


# Create your views here.
def home(request):
    template = 'homepage/home.html'
    items = (catalog.models.Item.objects
             .filter(is_on_main=True)
             .order_by('name',)
             .select_related('category')
             .prefetch_related('tags'))

    context = {
        'items': items,
    }
    return render(request, template, context)


def coffee(request):
    return HttpResponse(
        "<h1>Я чайник</h1>",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
