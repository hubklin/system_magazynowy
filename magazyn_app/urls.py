from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produkty/', views.lista_produktow, name="lista_prodktow")
]

