from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cat/', views.listar_categorias, name='listar_categorias'),
    path('usuarios/nuevo/', views.user_new, name='usuario_nuevo'),
    path('usuarios/ajax/borra/usuario/', views.elimina_usuario, name='elimina_usuario'),
]
