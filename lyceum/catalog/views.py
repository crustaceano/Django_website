from django.http import HttpResponse


# Create your views here.
def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, element):
    return HttpResponse("<body>" + f"Подробно об элементе {element}" + "</body>")
