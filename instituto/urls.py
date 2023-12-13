from django.urls import path
from .views import instituto_list, instituto_create, instituto_update, instituto_delete
from . import views

urlpatterns = [
    path('listar/', instituto_list, name='instituto_list'),
    path('crear/', instituto_create, name='instituto_create'),
    path('<int:id>/editar/', views.instituto_update, name='instituto_update'),
    path('<int:id>/borrar/', instituto_delete, name='instituto_delete'),
]
