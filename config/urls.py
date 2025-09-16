from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Rotas de login
    path('login/estabelecimento/', views.login_estabelecimento, name='login_estabelecimento'),
    path('login/instituicao/', views.login_instituicao, name='login_instituicao'),

    # Rota de logout
    path('logout/', views.logout_view, name='logout'),
]
