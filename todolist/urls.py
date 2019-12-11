from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_notas'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cat/', views.listar_categorias, name='listar_categorias'),
]
