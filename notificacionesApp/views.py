from django.shortcuts import render

def lista_notificaciones(request):
    return render(request, 'notificaciones/lista_notificaciones.html')
