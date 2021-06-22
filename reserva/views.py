from django.shortcuts import render, redirect
from .models import Client
from .forms import RegistroForm
from django.template import RequestContext
from django.utils import timezone
from django.http import HttpResponse


def menu(request):
    return render(request, 'reserva/menu.html', {})

def simple(request):
    return render(request, 'reserva/Simple.html', {})

def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = Client (rut_client=form.cleaned_data['rut_client'],
                                first_name=form.cleaned_data['first_name'],
                                last_name=form.cleaned_data['last_name'],
                                phone=form.cleaned_data['phone'],
                                email=form.cleaned_data['email'])
            registro.save()
            return redirect('menu')
    else:   
        form = RegistroForm()                 
        return render(request,'reserva/formulario.html', {'form': form})

def login(request):
    return render(request, 'reserva/login.html', {})

def registro(request):
    return render(request, 'reserva/registro.html', {})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            registro = Client (rut_client=form.cleaned_data['rut_client'],
                                first_name=form.cleaned_data['first_name'],
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            registro.save()
            return redirect('menu')
    else:   
        form = RegistroForm()                
        return render(request,'reserva/registro.html', {'form': form})

# Create your views here.


