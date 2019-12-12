from django.shortcuts import render
from todolist.models import Usuario, Categoria, Nota

def listar_notas(request):
    listado_notas = Nota.objects.all()
    return render(request, 'todolist/lista_notas.html', {'task_list': listado_notas})

def listar_usuarios(request):
    listado_usuarios = Usuario.objects.all()
    return render(request, 'todolist/lista_usuarios.html', {'users_list': listado_usuarios})

def listar_categorias(request):
    listado_categorias = Categoria.objects.all()
    return render(request, 'todolist/lista_categorias.html', {'cat_list': listado_categorias})
