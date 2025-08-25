from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),        # Rotas do seu app core
    path('accounts/', include('allauth.urls')), # Rotas de login social (Google, etc)
]
