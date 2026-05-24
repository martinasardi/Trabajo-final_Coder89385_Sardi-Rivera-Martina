from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Post, Comentario, Perfil
from .forms import PostForm, PerfilForm, UserUpdateForm 

def home(request):
    """Muestra el muro de posts con buscador integrado y sus comentarios."""
    termino_busqueda = request.GET.get('buscar', '')
    if termino_busqueda:
        posts = Post.objects.filter(titulo__icontains=termino_busqueda) | Post.objects.filter(contenido__icontains=termino_busqueda)
    else:
        posts = Post.objects.all()
        
    posts = posts.order_by('-fecha')
    
    for post in posts:
        post.lista_comentarios = Comentario.objects.filter(post=post).order_by('-fecha') # type: ignore
        
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    """Página de información 'Acerca de mí'."""
    return render(request, 'blog/about.html')

def cafes_cerca(request):
    """Sección informativa de cafeterías recomendadas."""
    return render(request, 'blog/cafes_cerca.html')



def login_request(request):
    """Inicia sesión para usuarios registrados."""
    error_mensaje = None
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('home')
        else: 
            error_mensaje = "Usuario o contraseña incorrectos."
    else: 
        form = AuthenticationForm()
        
    return render(request, "blog/login.html", {"form": form, "error_mensaje": error_mensaje})


def logout_request(request):
    """Cierra la sesión activa de la cuenta."""
    logout(request)
    return redirect('home')


def register(request):
    """Crea una nueva cuenta validando disponibilidad de username y email."""
    if request.method == 'POST':
        username_or_email = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return render(request, 'blog/register.html', {'error_usuario': 'Las contraseñas no coinciden.'})

        if len(username_or_email) < 8:
            return render(request, 'blog/register.html', {'error_usuario': 'El usuario o email debe tener al menos 8 caracteres.'})
        
        if len(password1) <= 8:
            return render(request, 'blog/register.html', {'error_usuario': 'La contraseña debe ser más larga de 8 caracteres.'})

        usuario_por_username = User.objects.filter(username=username_or_email).exists()
        usuario_por_email = User.objects.filter(email=username_or_email).exists()

        if usuario_por_username or usuario_por_email:
            return render(request, 'blog/register.html', {'error_usuario': 'Ese nombre de usuario o email ya existe. Por favor, elegí otro.'})

        nuevo_usuario = User(
            username=username_or_email,
            email=username_or_email,
            password=make_password(password1)
        )
        nuevo_usuario.save()
        return redirect('login') 

    return render(request, 'blog/register.html')


@login_required
def ver_perfil(request):
    """Visualiza la información del perfil del usuario actual."""
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'blog/ver_perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    """Modifica y guarda los datos de usuario y avatar de forma persistente."""
    perfil_actual, created = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_actual)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('/perfil/') 
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil_actual)

    return render(request, 'blog/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


@login_required
def crear_post(request):
    """Permite publicar una nueva reseña o cafetería en el muro."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_post = form.save(commit=False)
            nuevo_post.autor = request.user
            nuevo_post.save()
            return redirect('home')
    else: 
        form = PostForm()
        
    return render(request, 'blog/crear_post.html', {'form': form})


@login_required
def agregar_comentario(request, post_id):
    """Añade una respuesta rápida a una publicación específica."""
    if request.method == "POST":
        texto = request.POST.get('texto_comentario')
        if texto:
            post = Post.objects.get(id=post_id)
            Comentario.objects.create(post=post, autor=request.user.username, texto=texto)
    return redirect('home')