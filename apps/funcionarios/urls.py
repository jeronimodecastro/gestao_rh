from django.urls import path
from .views import (
    FuncionariosCreateView,
    FuncionariosListView,
    FuncionariosUpdateView,
    FuncionariosDeleteView
)
from .views import pdf_reportlab, PdfHtml2Pdf, PdfHtml2PdfDebugView, ExpCsvView, ExpXlsView

urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosUpdateView.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDeleteView.as_view(), name='delete_funcionario'),
    path('novo/', FuncionariosCreateView.as_view(), name='create_funcionario'),
    path('pdf-reportlab/', pdf_reportlab, name='pdf_reportlab'),
    path('pdf-html2pdf/', PdfHtml2Pdf.as_view(), name='pdf_html2pdf'),
    path('pdf-html2pdf-debuf/', PdfHtml2PdfDebugView.as_view(), name='pdf_html2pdf_debug'),
    path('exp-csv', ExpCsvView.as_view(), name='exp_csv'),
    path('exp-xls', ExpXlsView.as_view(), name='exp_xls'),
]
