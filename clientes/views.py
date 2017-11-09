from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

def index(request):
	lista_clientes= Cliente.objects.order_by('nombre')
	context= {'lista_clientes': lista_clientes}
	return render(request, 'clientes/contactos.html', context)