from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar, name='agendar'),
    path('horarios_disponiveis/', views.horarios_disponiveis, name='horarios_disponiveis'),
]