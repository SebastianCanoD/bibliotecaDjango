from rest_framework import serializers
from apibiblioteca.models import Autor, Categoria, Libro
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Serializador para el modelo Autor
class AutorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Autor.
    Convierte los objetos de Autor en formatos JSON y viceversa.
    """
    class Meta:
        model = Autor
        fields = '__all__'  # Incluye todos los campos del modelo Autor.
        read_only_fields = ('id',)  # El campo 'id' solo es de lectura.

# Serializador para el modelo Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Categoria.
    Permite la conversión de datos del modelo a JSON y viceversa.
    """
    class Meta:
        model = Categoria
        fields = '__all__'  # Incluye todos los campos del modelo Categoria.
        read_only_fields = ('id',)  # El campo 'id' solo es de lectura.

# Serializador para el modelo Libro
class LibroSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = '__all__'  # Incluye todos los campos del modelo Libro

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url  # Devuelve la URL completa de la imagen
        return None


# Serializador para el modelo User (usuario del sistema)
class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User, que incluye manejo de contraseñas
    y creación de tokens de autenticación.
    """
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},  # La contraseña es de solo escritura.
        }

    def create(self, validated_data):
        """
        Crea un usuario con la contraseña encriptada y genera un token de autenticación.
        """
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Genera un token de autenticación para el usuario.

        return user
