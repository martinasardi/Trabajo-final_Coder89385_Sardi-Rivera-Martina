from django import forms
from django.contrib.auth.models import User 
from .models import Post, Perfil

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'metodo_preparacion', 'puntuacion' ,'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;', 'placeholder': 'Ej: Escala Café'}),
            'subtitulo': forms.TextInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;', 'placeholder': 'Ej: Café de especialidad en Nueva Córdoba'}),
            'contenido': forms.Textarea(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px; height:150px;', 'placeholder': 'Contanos qué tal el café, el ambiente...'}),
            'metodo_preparacion': forms.Select(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
            'puntuacion': forms.Select(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
            'imagen': forms.FileInput(attrs={'style': 'margin-bottom:20px;'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']
        labels = {'avatar': 'Foto de Perfil (Avatar)'}
    
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'style': 'margin-bottom:20px;',
                'class': 'buscador-cafe'
            })
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico'
        }
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
            'first_name': forms.TextInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
            'last_name': forms.TextInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
            'email': forms.EmailInput(attrs={'class': 'buscador-cafe', 'style': 'margin-bottom:15px;'}),
        }