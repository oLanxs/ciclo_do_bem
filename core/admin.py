from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Campos que vão aparecer na lista do admin
    list_display = ('email', 'tipo', 'is_staff', 'is_active')
    list_filter = ('tipo', 'is_staff', 'is_active')
    
    # Campos usados no formulário de criação/edição
    fieldsets = (
        (None, {'fields': ('email', 'password', 'tipo')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    # Campos para criar usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tipo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
