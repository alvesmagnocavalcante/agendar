from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('barbearia.urls')),
    path('horarios/', include('barbearia.urls')),
]