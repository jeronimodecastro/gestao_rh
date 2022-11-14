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

