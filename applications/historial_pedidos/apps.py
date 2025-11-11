from django.apps import AppConfig

class HistorialPedidosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.historial_pedidos'  # ← Nombre completo con applications
    verbose_name = 'Historial de Pedidos'