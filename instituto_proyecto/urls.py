
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views     


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('institutos/', include('instituto.urls')),
    path('carreras/', include('carrera.urls')),
    path('materias/', include('materia.urls')),
]
