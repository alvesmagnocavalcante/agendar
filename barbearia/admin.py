from django.contrib import admin
from .models import Agendamento

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['hora', 'disponivel']

admin.site.register(Agendamento, AgendamentoAdmin)