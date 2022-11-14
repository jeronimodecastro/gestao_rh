from django.urls import path
from .views import (
    DepartamentosCreateView,
    DepartamentosListView,
    DepartamentosUpdateView,
    DepartamentosDeleteView,
)


urlpatterns = [
    path('', DepartamentosListView.as_view(), name='list_departamentos'),
    path('editar/<int:pk>/', DepartamentosUpdateView.as_view(), name='update_departamento'),
    path('deletar/<int:pk>/', DepartamentosDeleteView.as_view(), name='delete_departamento'),
    path('novo/', DepartamentosCreateView.as_view(), name='create_departamento'),
]