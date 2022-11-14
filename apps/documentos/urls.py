from django.urls import path
from .views import (
    DocumentosCreateView
)


urlpatterns = [
    path('novo/<int:id_funcionario>/', DocumentosCreateView.as_view(), name='create_documento'),
]