from rest_framework import routers
from apibiblioteca.views import (
    AutorViewSet,
    CategoriaViewSet,
    LibroViewSet,
    UserViewSet,
    LogoutView,
    LoginView
)
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

# Registro de rutas con el router de DRF
router = routers.DefaultRouter()
router.register('autores', AutorViewSet)  # Ruta para Autores
router.register('categorias', CategoriaViewSet)  # Ruta para Categorías
router.register('libros', LibroViewSet)  # Ruta para Libros
router.register('usuarios', UserViewSet)  # Ruta para Usuarios

# Definición de urlpatterns
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Obtener token
    path('login/', LoginView.as_view(), name='login'),  # Inicio de sesión
    path('logout/', LogoutView.as_view(), name='logout'),  # Cierre de sesión
] + router.urls
