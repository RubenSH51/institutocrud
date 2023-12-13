from django.urls import path
from .views import carrera_list, carrera_create, carrera_update, carrera_delete
from . import views

urlpatterns = [
    path('listar/', carrera_list, name='carrera_list'),
    path('crear/', carrera_create, name='carrera_create'),
    path('<int:id>/editar/', views. carrera_update, name='carrera_update'),
    path('<int:id>/borrar/', carrera_delete, name='carrera_delete'),
]