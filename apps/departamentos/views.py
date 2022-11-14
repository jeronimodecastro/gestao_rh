from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Departamento


class DepartamentosListView(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosUpdateView(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentosDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')


class DepartamentosCreateView(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)  # Commit=False serve para não enviar para o banco de dados.
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreateView, self).form_valid(form)

