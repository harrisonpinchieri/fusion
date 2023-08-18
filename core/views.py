from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .models import Servico, Funcionario, Features
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()

        var = int((Features.objects.count()) / 2)
        context['feature1'] = Features.objects.all()[:var]
        context['feature2'] = Features.objects.all()[var:]

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
