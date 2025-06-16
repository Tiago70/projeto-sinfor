from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdminNew(UserAdmin):
    model = User
    list_display = ['email', 'nome', 'cnpj', 'telefone', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    ordering = ['nome']
    search_fields = ['email', 'nome', 'cnpj']

    fieldsets = (
        ('Informações do cadastro', {'fields': ('email', 'password')}),
        ('Informações da Empresa', {'fields': ('nome', 'cnpj', 'telefone')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'cnpj', 'telefone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, UserAdminNew)
