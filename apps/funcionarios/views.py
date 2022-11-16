import csv
import io

import xlwt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    TemplateView
)
from reportlab.pdfgen import canvas
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .models import Funcionario


class FuncionariosListView(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionariosDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionariosCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)  # Commit=False serve para não enviar para o banco de dados.
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.usuario = User.objects.create(username=funcionario.nome)
        funcionario.save()
        return super(FuncionariosCreateView, self).form_valid(form)


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachament; filename="rel_funcionarios.pdf"'  # serve para baixar o arquivo

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatório de Funcionários')

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    campos = 'Nome: %s | Hora Extra %.2f'

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, campos % (funcionario.nome, funcionario.total_horas_extras))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Erro renderizando PDF", status=400)


class PdfHtml2Pdf(View):
    def get(self, request):
        funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

        params = {
            'data': funcionarios,
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'rel_funcionarios')


class PdfHtml2PdfDebugView(TemplateView):
    template_name = 'funcionarios/relatorio.html'


class ExpCsvView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=funcionarios.csv'

        funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

        writer = csv.writer(response)
        writer.writerow(['Nome', 'Total Horas'])
        for funcionario in funcionarios:
            writer.writerow([funcionario.nome, funcionario.total_horas_extras])
        return response


class ExpXlsView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=funcionarios.xls'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Funcionarios', cell_overwrite_ok=True)

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        colums = ['id', 'nome', 'Total de Horas']

        for col_num in range(len(colums)):
            ws.write(row_num, col_num, colums[col_num], font_style)

        font_style = xlwt.XFStyle()

        funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

        row_num = 1
        for funcionario in funcionarios:
            ws.write(row_num, 0, funcionario.id, font_style)
            ws.write(row_num, 1, funcionario.nome, font_style)
            ws.write(row_num, 2, funcionario.total_horas_extras, font_style)
            row_num += 1
        wb.save(response)
        return response

