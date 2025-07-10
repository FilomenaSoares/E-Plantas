from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Configuração para exibir e editar o CustomUser no painel de administração.
    """
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Papel Customizado', {'fields': ('role',)}),
    )
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    
    list_filter = UserAdmin.list_filter + ('role',)

admin.site.register(CustomUser, CustomUserAdmin)