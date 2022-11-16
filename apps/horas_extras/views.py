import json

from django.http import HttpResponse
from django.views import View
from .forms import HorasExtrasForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import HoraExtra


class HorasExtrasListView(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HorasExtrasFuncionariosUpdateView(UpdateView):
    model = HoraExtra
    form_class = HorasExtrasForm
    # success_url = reverse_lazy('update_funcionario')

    def get_success_url(self):
        return reverse_lazy('update_funcionario', args=[self.object.funcionario.id])

    def get_form_kwargs(self):
        kwargs = super(HorasExtrasFuncionariosUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HorasExtrasUpdateView(UpdateView):
    model = HoraExtra
    form_class = HorasExtrasForm

    def get_form_kwargs(self):
        kwargs = super(HorasExtrasUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HorasExtrasDeleteView(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_horas_extras')


class HorasExtrasCreateView(CreateView):
    model = HoraExtra
    form_class = HorasExtrasForm

    def get_form_kwargs(self):
        kwargs = super(HorasExtrasCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtraView(View):
    def post(self, *args, **kwargs):
        he = HoraExtra.objects.get(id=kwargs['pk'])
        he.utilizada = True
        he.save()

        funcionario = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Hora extra marcada como utilizada',
             'horas': float(funcionario.total_horas_extras)}
        )
        return HttpResponse(response, content_type='application/json')


class NaoUtilizouHoraExtraView(View):
    def post(self, *args, **kwargs):
        he = HoraExtra.objects.get(id=kwargs['pk'])
        he.utilizada = False
        he.save()

        funcionario = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Hora extra marcada como não utilizada',
             'horas': float(funcionario.total_horas_extras)}
        )
        return HttpResponse(response, content_type='application/json')
