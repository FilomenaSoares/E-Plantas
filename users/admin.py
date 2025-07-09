from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Configuração para exibir e editar o CustomUser no painel de administração.
    """
    # Adiciona o campo 'role' aos formulários de criação e edição de usuário.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Papel Customizado', {'fields': ('role',)}),
    )
    
    # Adiciona 'role' à lista de colunas na visualização de usuários.
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    
    # Adiciona um filtro pela coluna 'role'.
    list_filter = UserAdmin.list_filter + ('role',)

# Registra o modelo CustomUser com a sua configuração customizada.
admin.site.register(CustomUser, CustomUserAdmin)