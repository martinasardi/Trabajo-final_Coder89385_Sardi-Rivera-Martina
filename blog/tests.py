from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Metodo, Comentario

class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester_cafe', password='password123')
        
        self.metodo = Metodo.objects.create(
            nombre='Prensa Francesa',
            descripcion='Extracción por inmersión.'
        )
        
        self.post = Post.objects.create(
            titulo='Café de Especialidad Colombiano',
            contenido='Cuerpo medio, notas a chocolate.',
            autor=self.user,
            metodo_preparacion=self.metodo,
            puntuacion=5
        )

    def test_post_creation(self):
        post_guardado = Post.objects.get(id=self.post.id) # type: ignore
        self.assertEqual(post_guardado.titulo, 'Café de Especialidad Colombiano')

    def test_post_string_representation(self):
        self.assertEqual(str(self.post), self.post.titulo)

    def test_comentario_integration_flow(self):
        """Prueba de Integración: Simula el envío del formulario de comentarios"""
        self.client.login(username='tester_cafe', password='password123')
        url = reverse('agregar_comentario', kwargs={'post_id': self.post.id})
        response = self.client.post(url, {'texto_comentario': 'Me encantó esta cafetería.'})
        
        self.assertEqual(response.status_code, 302)
        comentario_creado = Comentario.objects.filter(post=self.post).first()
        self.assertIsNotNone(comentario_creado)
        self.assertEqual(comentario_creado.texto, 'Me encantó esta cafetería.') # type: ignore