from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required



def inicio(request):

    reservas_usuario = []

    if request.user.is_authenticated:
        reservas_usuario = Reserva.objects.filter(usuario = request.user).order_by('fecha', 'horario')

    context = {
        'reservas_usuario': reservas_usuario,
    }

    return render(
        request,
        'reservas/inicio.html',
        context
    )

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)

    return render(
        request,
        'reservas/lista_reservas.html',
        {'reservas': reservas}
    ) 

@login_required
def crear_reserva(request):

    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
           reserva = form.save(commit=False)
           
           reserva.usuario = request.user
           
           reserva.save()
           
           messages.success(
                request,
                'Reserva creada correctamente.'
            )
           
           return redirect('lista_reservas')
    else:
        form = ReservaForm()
    
    return render(
        request,
        'reservas/crear_reserva.html',
        {'form':form}
    )

def editar_reserva(request, id):

    reserva = get_object_or_404(
        Reserva,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = ReservaForm(
            request.POST,
            instance=reserva
            )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Reserva actualizada correctamente.'
            )
            return redirect('lista_reservas')
    
    else:
        form = ReservaForm(instance=reserva)
    return render(
        request,
        'reservas/editar_reserva.html',
        {'form':form}
    )

def eliminar_reserva(request, id):
     
    reserva = get_object_or_404(
        Reserva,
        id=id,
        usuario=request.user
    )
        
    if request.method == 'POST':
        reserva.delete()
        messages.success(
            request,
            'Reserva eliminada correctamente'
        )
        return redirect('lista_reservas')

    return render(
        request,
        'reservas/eliminar_reserva.html',
        {'reserva':reserva}
    )

def registro(request):

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            messages.success(
                request,
                'Usuario registrado crrectamente'
            )

            return redirect('inicio')
        
    else:
        form = RegistroUsuarioForm()
    
    return render(
        request,
        'registration/registro.html',
        {'form':form}
    )