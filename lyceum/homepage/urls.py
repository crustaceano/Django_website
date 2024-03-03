from django.urls import path
from . import views
app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='homepage_main'),
    path('cofee/', views.cofee, name='homepage_cofeepoint'),
]

