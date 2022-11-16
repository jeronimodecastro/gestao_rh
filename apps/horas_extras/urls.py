from django.urls import path
from .views import (
    HorasExtrasCreateView,
    HorasExtrasListView,
    HorasExtrasUpdateView,
    HorasExtrasDeleteView,
    HorasExtrasFuncionariosUpdateView,
    UtilizouHoraExtraView,
    NaoUtilizouHoraExtraView
)


urlpatterns = [
    path('', HorasExtrasListView.as_view(), name='list_horas_extras'),
    path('editar/<int:pk>/', HorasExtrasUpdateView.as_view(), name='update_hora_extra'),
    path('utilizou-he/<int:pk>/', UtilizouHoraExtraView.as_view(), name='utilizou_he'),
    path('nao-utilizou-he/<int:pk>/', NaoUtilizouHoraExtraView.as_view(), name='nao_utilizou_he'),
    path('editar_he_funcionario/<int:pk>/', HorasExtrasFuncionariosUpdateView.as_view(),
         name='update_hora_extra_funcionario'),
    path('deletar/<int:pk>/', HorasExtrasDeleteView.as_view(), name='delete_hora_extra'),
    path('novo/', HorasExtrasCreateView.as_view(), name='create_hora_extra'),
]