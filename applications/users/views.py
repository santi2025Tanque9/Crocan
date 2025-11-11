from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from applications.historial_pedidos.models import Order, OrderItem

from applications.historial_pedidos.models import Order, OrderItem

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



@login_required
def historial_pedidos(request):
    """Vista para mostrar el historial de pedidos del socio"""
    # Obtener todos los pedidos del usuario, ordenados por fecha descendente
    pedidos = Order.objects.filter(customer=request.user).select_related().prefetch_related('items')
    
    # Calcular estadísticas
    total_pedidos = pedidos.count()
    total_gastado = sum(pedido.total for pedido in pedidos)
    total_puntos_ganados = sum(pedido.points_earned for pedido in pedidos)
    
    context = {
        'pedidos': pedidos,
        'total_pedidos': total_pedidos,
        'total_gastado': total_gastado,
        'total_puntos_ganados': total_puntos_ganados,
    }
    
    return render(request, 'users/historial_pedidos.html', context)

@login_required
def detalle_pedido(request, pedido_id):
    """Vista para mostrar los detalles de un pedido específico"""
    try:
        pedido = Order.objects.get(id=pedido_id, customer=request.user)
        items_pedido = pedido.items.all().select_related('product')
    except Order.DoesNotExist:
        return redirect('users_app:historial_pedidos')
    
    context = {
        'pedido': pedido,
        'items_pedido': items_pedido,
    }
    
    return render(request, 'users/detalle_pedido.html', context)