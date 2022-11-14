from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
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
