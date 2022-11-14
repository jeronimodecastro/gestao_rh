from django.urls import path
from .views import (
    FuncionariosCreateView,
    FuncionariosListView,
    FuncionariosUpdateView,
    FuncionariosDeleteView,
)


urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosUpdateView.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDeleteView.as_view(), name='delete_funcionario'),
    path('novo/', FuncionariosCreateView.as_view(), name='create_funcionario'),
]