from django.shortcuts import render

def listar_notas(request):
    return render(request, 'todolist/lista_notas.html', {})

def listar_usuarios(request):
    return render(request, 'todolist/lista_usuarios.html', {})

def listar_categorias(request):
    return render(request, 'todolist/lista_categorias.html', {})
