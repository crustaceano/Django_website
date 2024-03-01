from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage_main'),
    path('cofee/', views.cofee, name='homepage_cofeepoint'),
]

