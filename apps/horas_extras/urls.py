from django.urls import path
from .views import (
    HorasExtrasCreateView,
    HorasExtrasListView,
    HorasExtrasUpdateView,
    HorasExtrasDeleteView,
    HorasExtrasFuncionariosUpdateView
)


urlpatterns = [
    path('', HorasExtrasListView.as_view(), name='list_horas_extras'),
    path('editar/<int:pk>/', HorasExtrasUpdateView.as_view(), name='update_hora_extra'),
    path('editar_he_funcionario/<int:pk>/', HorasExtrasFuncionariosUpdateView.as_view(),
         name='update_hora_extra_funcionario'),
    path('deletar/<int:pk>/', HorasExtrasDeleteView.as_view(), name='delete_hora_extra'),
    path('novo/', HorasExtrasCreateView.as_view(), name='create_hora_extra'),
]