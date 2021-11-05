from typing import overload
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import PessoaForm, MusicaForm

def index(request):
    nome = request.GET.get('nome')
    print(request.GET)
    return render(request, 'core/index.html')

class AboutView(View):
    def get(self, request):
        print(request.GET.get('chave'))
        return HttpResponse('result')

    def post(self, request):
        print(request.GET.get('chave'))
        return HttpResponse('post')

@method_decorator(login_required(login_url='core:index'), name='dispatch')
class MyFormView(View):
    form_class = ""
    initial = {}
    template_name = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, "core/" + self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, "core/" + self.template_name, {'form': form})

class PessoaFormView(MyFormView):
    form_class = PessoaForm
    initial = {'nome':'joao'}
    template_name = 'cadastrar_pessoa.html'

class MusicaFormView(MyFormView):
    form_class = MusicaForm
    initial = {'nome':'song'}
    template_name = 'cadastrar_musica.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, "core/" + self.template_name, {'form': form})

