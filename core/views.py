from typing import overload
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import PessoaForm, MusicaForm
from .models import Pessoa

def index(request):
    nome = request.GET.get('nome')
    print(request.GET)
    return render(request, 'core/index.html')

class PessoaList(ListView):
    model = Pessoa
    context_object_name = 'pessoas_cadastradas'

