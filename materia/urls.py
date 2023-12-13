from django.urls import path
from .views import materia_list, materia_create, materia_update, materia_delete
from . import views

urlpatterns = [
    path('listar/', materia_list, name='materia_list'),
    path('crear/', materia_create, name='materia_create'),
    path('<int:id>/editar/', views.materia_update, name='materia_update'),
    path('<int:id>/borrar/', materia_delete, name='materia_delete'),
]