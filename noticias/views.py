from django.shortcuts import render, redirect
from multiprocessing import context
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import NoticiaForm
import inspect

from .models import Noticia, Categoria
# Create your views here.


def index(request):
    context= {}
    return render (request, 'noticias/index.html', context)

# def noticia(request):
#     context= {}
#     return render (request, 'noticias/noticia.html', context)

def noticia(request, id_categoria):
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    noticias = Noticia.objects.filter(id_categoria=categoria)

    context = {
        'categoria': categoria,
        'noticia': noticias,  # Cambiar 'noticias' a 'noticia'
    }
    return render(request, 'noticias/noticia.html', context)


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

def edit(request, id_noticia):
    noticia = Noticia.objects.get(id_noticia=id_noticia)
    formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
    if formulario.is_valid() and request.POST:
         formulario.save()
         return redirect('listado')
    return render(request, "noticias/gestion/editarNoticia.html", {"formulario": formulario})

    
    
# def edit(request, id_noticia):
#      noticia = Noticia.objects.get(id_noticia_id=id_noticia)
#      formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
#      if formulario.is_valid() and request.POST:
#         formulario.save()
#         return redirect('listado')
#      return render(request, "noticias/gestion/editarNoticia.html", {"formulario": formulario})

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
