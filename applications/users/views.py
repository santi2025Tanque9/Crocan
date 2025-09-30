
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('users_app:login')
    else:
        form = RegistroForm()
    return render(request, 'users/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        dni = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=dni, password=password)
        if user is not None:
            login(request, user)
            # CAMBIO IMPORTANTE: Redirigir a la lista de productos en lugar del home
            return redirect('products:product_list')  # Cambiado esta línea
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def home(request):
    # Esta vista ya no se usa para el home principal
    return render(request, 'users/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users_app:login')

def home(request):
    # Cambiar para que redirija al home en lugar de a productos
    return render(request, 'home.html')