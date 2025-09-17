from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Logins
    path('login/estabelecimento/', views.login_estabelecimento, name='login_estabelecimento'),
    path('login/instituicao/', views.login_instituicao, name='login_instituicao'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards
    path('dashboard/estabelecimento/', views.dashboard_estabelecimento, name='dashboard_estabelecimento'),
    path('dashboard/instituicao/', views.dashboard_instituicao, name='dashboard_instituicao'),

    # 🔹 Página "Saiba Mais"
    path('saiba-mais/', views.saiba_mais, name='saiba_mais'),
]
