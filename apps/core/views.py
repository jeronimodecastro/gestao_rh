from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from apps.horas_extras.models import HoraExtra

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionario = request.user.funcionario
    data['total_funcionarios'] = funcionario.empresa.total_funcionarios
    data['total_funcionarios_ferias'] = funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_pendente'] = funcionario.empresa.total_funcionarios_doc_pendente
    data['total_funcionarios_doc_ok'] = funcionario.empresa.total_funcionarios_doc_ok
    data['total_funcionarios_doc_rg'] = 5
    data['total_he_pendente'] = HoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=False).aggregate(
        Sum('horas'))['horas__sum'] or 0
    data['total_he_utilizada'] = HoraExtra.objects.filter(
        funcionario__empresa=funcionario.empresa, utilizada=True).aggregate(
        Sum('horas'))['horas__sum'] or 0
    return render(request, 'core/index.html', data)
