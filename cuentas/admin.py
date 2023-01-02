# by: RETBOT
#cuentas/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCambioUsuario, FormularioCreacionUsuario
from .models import UsuarioPers
# by: RETBOT
# Register your models here.
class UsuarioPersAdmin(UserAdmin):
    add_form = FormularioCreacionUsuario
    form = FormularioCambioUsuario
    model = UsuarioPers
    list_display = ['email', 'username', 'edad', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('edad',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('edad',)}),
    )

admin.site.register(UsuarioPers, UsuarioPersAdmin)
# by: RETBOT
