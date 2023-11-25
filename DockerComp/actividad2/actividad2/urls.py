from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Asumiendo que 'usuarios' es el nombre de tu app
    # Agrega la siguiente línea para manejar la URL raíz
    path('', include('usuarios.urls')),  # Puedes ajustar esto según tu estructura
]
