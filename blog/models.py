from django.db import models
from django.contrib.auth.models import User

# Modelo 1: Métodos de preparación (V60, Prensa Francesa, etc.)
class Metodo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo 2: Las reseñas de café
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_preparacion = models.ForeignKey(Metodo, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='cafes/', blank=True, null=True)
    PUNTUACION_CHOICES = [
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
    ]
    puntuacion = models.IntegerField(choices=PUNTUACION_CHOICES, default=5, verbose_name="Calificación")

    def __str__(self):
        return self.titulo

# Modelo 3: Comentarios de los usuarios
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"
    
#Modelo 4: Perfil extendido con foto
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    
    def __str__(self): return f"Perfil de {self.usuario.username}"
