from django.urls import path
from .views import EmpresaCreateView, EmpresaEditView


urlpatterns = [
    path('novo', EmpresaCreateView.as_view(), name='create_empresa'),
    path('editar/<int:pk>', EmpresaEditView.as_view(), name='edit_empresa'),
]