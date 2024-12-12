from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication, status, views, response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from apibiblioteca.models import Autor, Categoria, Libro
from apibiblioteca.serializers import AutorSerializer, CategoriaSerializer, LibroSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# ViewSet para el modelo Autor
class AutorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las operaciones CRUD del modelo Autor.
    """
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para el modelo Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las operaciones CRUD del modelo Categoria.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para el modelo Libro
class LibroViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las operaciones CRUD del modelo Libro.
    Incluye las relaciones con Autor y Categoria.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [permissions.AllowAny]

# ViewSet para el modelo User
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para leer información de usuarios del sistema.
    Solo accesible para administradores.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.BasicAuthentication]

# Vista para manejar el inicio de sesión
class LoginView(views.APIView):
    """
    Vista para autenticar usuarios y generar tokens de sesión.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return response.Response(
                {'message': 'Ingrese su usuario y contraseña.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return response.Response(
                {'message': 'Usuario o contraseña incorrectos.'},
                status=status.HTTP_404_NOT_FOUND
            )

        token, _ = Token.objects.get_or_create(user=user)
        return response.Response(
            {'message': 'Inicio de sesión exitoso.', 'token': token.key},
            status=status.HTTP_200_OK
        )
@csrf_exempt
def mi_vista_sin_csrf(request):
    if request.method == 'POST':
        return HttpResponse("POST recibido sin protección CSRF")
    return HttpResponse("Usa un POST")
# Vista para manejar el cierre de sesión
class LogoutView(views.APIView):
    """
    Vista para cerrar sesión y eliminar el token de autenticación.
    """
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return response.Response(
            {'message': 'Su sesión se ha cerrado ¡Hasta pronto!.'},
            status=status.HTTP_200_OK
        )
