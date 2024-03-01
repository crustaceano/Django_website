import django.urls
from django.urls import path, re_path
from . import views
from . import converters
app_name = 'catalog'

django.urls.register_converter(
    converters.PositiveIntegerConverter,
    'positive',
)
urlpatterns = [
    path('catalog/', views.item_list, name='item_list'),
    path('catalog/<int:element>/', views.item_detail, name='item_detail'),
    # path('converter/<positive:element>/', views.item_detail),
    # re_path(r'^re/(?P<element>[1-9]\d*)/$', views.item_detail),
]