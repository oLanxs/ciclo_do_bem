from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      # Aqui usamos index
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
