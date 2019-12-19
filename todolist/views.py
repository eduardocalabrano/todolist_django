from django.shortcuts import render
from todolist.models import Usuario, Categoria, Nota
from django.http import JsonResponse
from .forms import UsuarioForm

def listar_notas(request):
    listado_notas = Nota.objects.all()
    return render(request, 'todolist/lista_notas.html', {'task_list': listado_notas})

def listar_usuarios(request):
    listado_usuarios = Usuario.objects.all()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            form = UsuarioForm()
            """Si se envía correctamente y posteriormente actualizo (F5) puede duplicarse el ingreso del dato. Por el momento solo lo evito por el unique=True del campo email"""
        else:
            """Falta saber como capturar un error, por ejemplo si no se cumple la condición unique del campo email y mostrar un mensaje en pantalla."""
            form = UsuarioForm()
    else:
        form = UsuarioForm()
    return render(request, 'todolist/lista_usuarios.html', {'users_list': listado_usuarios, 'form': form})

def listar_categorias(request):
    listado_categorias = Categoria.objects.all()
    return render(request, 'todolist/lista_categorias.html', {'cat_list': listado_categorias})

def user_new(request):
    form = UsuarioForm()
    return render(request, 'todolist/editar_usuario.html', {'form': form})

def elimina_usuario(request):
    id_usuario = request.GET.get('id', None)
    registro = Usuario.objects.get(pk=id_usuario)
    registro.delete()
    data = {
        'respuesta': 'Eliminación correcta'
    }
    return JsonResponse(data)
