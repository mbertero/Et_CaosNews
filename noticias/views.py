from django.shortcuts import render, redirect,HttpResponse
from multiprocessing import context
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import NoticiaForm
import inspect

from .models import Noticia, Categoria, Equipo, Comentario
# Create your views here.


def index(request):
    equipo = Equipo.objects.all()
    noticia = Noticia.objects.all()
    context = {
        'equipo': equipo, 'noticia': noticia,
    }
    return render (request, 'noticias/index.html', context)

# def noticia(request):
#     context= {}
#     return render (request, 'noticias/noticia.html', context)

def noticia(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)

    categoria = Categoria.objects.get(id_categoria=id_categoria)
    noticia = Noticia.objects.filter(id_categoria=categoria)

    context = {
        'categoria': categoria,
        'noticia': noticia,  
    }
    return render(request, 'noticias/noticia.html', context)

# def equipo(request):
#     equipo = Noticia.objects.all()
#     context={"noticia":noticia}
#     return render(request, 'noticias/gestion/listado.html', context)


## GESTION DE NOTICIAS
@login_required
def listado(request):
    noticia = Noticia.objects.all()
    context={"noticia":noticia}
    return render(request, 'noticias/gestion/listado.html', context)

    
def add(request):
    formulario = NoticiaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('listado')
    return render(request, "noticias/gestion/noticiasAdd.html", {"formulario": formulario})


from django.shortcuts import render, redirect

def edit(request, id_noticia):
    if request.method == 'POST':
        noticia = Noticia.objects.get(id_noticia=id_noticia)
        formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Noticia Actualizada!')
            return redirect('listado')
    else:
        # Manejar las solicitudes GET aquí
        noticia = Noticia.objects.get(id_noticia=id_noticia)
        formulario = NoticiaForm(instance=noticia)

    context = {'formulario': formulario}
    return render(request, 'noticias/gestion/editarNoticia.html', context)


def delete(request, id_noticia):
     noticia = Noticia.objects.get(id_noticia=id_noticia)
     noticia.delete()
     messages.success(request, '¡Noticia Eliminada!')
     return redirect('listado')
 
  
#GESTION USUARIOS
def login(request):
     return render(request, "registration/login.html")

def salir(request):
    logout(request)
    return redirect('/')
