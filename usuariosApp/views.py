from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from usuariosApp.models import Usuario

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('home')  # Cambia 'home' por la vista que deseas después del login
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    return render(request, 'usuarios/login.html')  # Actualizado para usar 'usuarios/login.html'

def logout_usuario(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('login')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    return render(request, 'usuarios/login.html')

from django.contrib.auth.decorators import login_required

@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})


from django.contrib.auth.models import User

@login_required
def lista_usuarios(request):
    if request.user.is_staff:
        usuarios = User.objects.all()
        return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})
    else:
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')

# Solo administradores pueden acceder
@user_passes_test(lambda u: u.is_staff, login_url='home')
def asignar_rol(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        nuevo_rol = request.POST.get('rol')
        if nuevo_rol == 'staff':
            usuario.is_staff = True
        else:
            usuario.is_staff = False
        usuario.save()
        messages.success(request, f"Rol actualizado correctamente para {usuario.username}.")
        return redirect('lista_usuarios')
    return render(request, 'usuarios/asignar_rol.html', {'usuario': usuario})

@user_passes_test(lambda u: u.rol == 'admin', login_url='home')
def asignar_rol(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    if request.method == 'POST':
        nuevo_rol = request.POST.get('rol')
        if nuevo_rol in dict(Usuario.ROLES).keys():  # Validar que el rol esté en las opciones
            usuario.rol = nuevo_rol
            usuario.save()
            messages.success(request, f"Rol actualizado correctamente para {usuario.username}.")
        else:
            messages.error(request, "Rol no válido.")
        return redirect('lista_usuarios')
    return render(request, 'usuarios/asignar_rol.html', {'usuario': usuario})

