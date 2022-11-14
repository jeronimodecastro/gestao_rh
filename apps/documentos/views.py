from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    CreateView
)
from .models import Documento


class DocumentosCreateView(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        form.instance.funcionario_id = self.kwargs['id_funcionario']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
