from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('about/', views.about, name='about'),
    path('nuevo-post/', views.crear_post, name='crear_post'),
    path('comentario/<int:post_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('cafes-cerca/', views.cafes_cerca, name='cafes_cerca'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
