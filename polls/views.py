from polls.models import Client
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }
    return render(request, 'polls/home.html', context)


def clientes(request):
    clientes = Client.objects.all()
    context = {
        'lista_clientes': clientes,
    }
    return render(request, 'polls/cliente.html', context)


def sitios(request):
    sitios = Site.objects.all()
    context = {
        'lista_sitios': sitios,
    }
    return render(request, 'polls/sitios.html', context)


def documentos(request):
    documentos = Documento.objects.all()
    context = {
        'lista_documentos': documentos,
    }
    return render(request, 'polls/documentos.html', context)


def oportunidades(request):
    oportunidades = Lead.objects.all()
    context = {
        'lista_oportunidades' : oportunidades
    }
    return render(request, 'polls/oportunidades.html', context)