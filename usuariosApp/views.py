from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroForm
from .models import Usuario

# Registro de usuario
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

# Login de usuario
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

# Logout de usuario
@login_required
def logout_usuario(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('home')

# Perfil de usuario
@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})

# Lista de usuarios (solo administrador)
@user_passes_test(lambda u: u.rol == 'admin', login_url='home')
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Asignar rol (solo administrador)
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
