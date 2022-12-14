from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .form import *

# Create your views here.

def home(request):
  data = {}
  data['transacoes'] = Transacao.objects.all()
  return render(request, 'contas/home.html', data)



def listagem(request):
  data = {}
  data['transacoes'] = Transacao.objects.all()
  return render(request, 'contas/listagem.html', data)



def nova_transacao(request):
  form = TransacaoForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('listagem')

  return render(request, 'contas/form.html', {'form': form})



def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
  
    if form.is_valid():
      form.save()
      return redirect('listagem')
   
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)



def delete(request, pk):
  transacao = Transacao.objects.get(pk=pk)
  transacao.delete()
  return redirect('listagem')