import django.urls

from . import views

app_name = 'feedback'

urlpatterns = [
    django.urls.path('', views.index, name='feedback')
]