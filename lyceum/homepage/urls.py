from django.urls import path
from . import views
app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='homepage_main'),
    path('coffee/', views.coffee, name='homepage_coffeepoint'),
]

