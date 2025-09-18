# ofertas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ofertas/', views.listar_ofertas, name='listar_ofertas'),
    path('ofertas/nova/', views.criar_oferta, name='criar_oferta'),
]
