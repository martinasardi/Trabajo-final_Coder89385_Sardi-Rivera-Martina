from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Metodo

class BlogTests(TestCase):

    def setUp(self):
        # 1. Creamos un usuario de prueba para el autor
        self.user = User.objects.create_user(username='tester_cafe', password='password123')
        
        # 2. Creamos un método de preparación de prueba
        self.metodo = Metodo.objects.create(
            nombre='Prensa Francesa',
            descripcion='Extracción por inmersión.'
        )
        
        # 3. Creamos el Post usando tus campos exactos
        self.post = Post.objects.create(
            titulo='Café de Especialidad Colombiano',
            subtitulo='Una delicia frutal',
            contenido='Cuerpo medio, notas a chocolate y frutos rojos.',
            autor=self.user,
            metodo_preparacion=self.metodo,
            puntuacion=5
        )

    def test_post_creation(self):
        """Valida que el post de café se guarde con los atributos correctos"""
        post_guardado = Post.objects.get(id=self.post.id)
        self.assertEqual(post_guardado.titulo, 'Café de Especialidad Colombiano')
        self.assertEqual(post_guardado.autor.username, 'tester_cafe')
        self.assertEqual(post_guardado.metodo_preparacion.nombre, 'Prensa Francesa')
        self.assertEqual(post_guardado.puntuacion, 5)

    def test_post_string_representation(self):
        """Valida que el método __str__ del Post devuelva el título"""
        self.assertEqual(str(self.post), self.post.titulo)