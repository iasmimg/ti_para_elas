from django.shortcuts import render, redirect
from .models import Acao
from .forms import AcaoForm

def listar_acao(request):
    acoes = Acao.objects.all()
    contexto = {
        'todas_acoes': acoes
    }
    return render(request, 'acao.html', contexto)

def cadastrar_acao(request):
    form = AcaoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_acao')

    contexto = {
        'form_acao': form
    }
    return render(request, 'acao_cadastrar.html', contexto)

def editar_acao(request, id):
    acao = Acao.objects.get(pk=id)

    form = AcaoForm(request.POST or None,  request.FILES or None ,instance=acao)

    if form.is_valid():
        form.save()
        return redirect('listar_acao')

    contexto = {
        'form_acao': form
    }

    return render(request, 'acao_cadastrar.html', contexto)
