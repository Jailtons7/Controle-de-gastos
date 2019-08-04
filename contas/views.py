from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm

import datetime

# Create your views here.
def horas(request):
    now = datetime.datetime.now()
    html = "<html><bod>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    data = {}
    data['transacoes'] = ['trans1', 'trans2', 'trans3']
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def novaTransacao(request):
    dados = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('urlListagem')

    dados['form'] = form
    return render(request, 'contas/form.html', dados)

def update(request, pk):
    dados = {}

    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('urlListagem')

    dados['form'] = form
    return render(request, 'contas/form.html', dados)