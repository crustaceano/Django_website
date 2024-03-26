from django.http import HttpResponse
import django.shortcuts
import catalog.models


# Create your views here.
def item_list(request):
    template = 'catalog/list.html'
    # items = catalog.models.Item.objects.only('name', 'text', 'category', 'id')
    # items = catalog.models.Item.objects.select_related('category').only('name', 'text', 'id', 'category__name')
    items = (catalog.models.Item.objects
             .filter(is_published=True)
             .select_related('category')
             .only('name', 'text', 'category__name')
             .select_related('main_image')
             # .prefetch_related('tags')
             .order_by('category__name')
             )
    # items = catalog.models.Item.objects.all()
    context = {
        'items': items,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, element):
    template = 'catalog/item_descriptions.html'
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.all(),
        pk=element)
    context = {
        'item': item,
    }
    return django.shortcuts.render(request, template, context)
