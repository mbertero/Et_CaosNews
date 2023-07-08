from django.shortcuts import render, redirect,HttpResponse
from multiprocessing import context
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import NoticiaForm
from django.contrib.auth.decorators import user_passes_test


from django.http import JsonResponse

import inspect, requests, json, urllib

from .models import Noticia, Categoria, Equipo, Comentario
# Create your views here.



def index(request):
    equipo = Equipo.objects.all()
    categorias = Categoria.objects.all()
    noticia = Noticia.objects.all()
    
    context = {
        'equipo': equipo,
        'categorias': categorias,
        'noticia': noticia,
    }
    
    if request.method == 'POST':
        city = request.POST["city"]
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&lang=es&APPID=d836e1ed4974036625c88987913d9419').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)

        return render(request, "noticias/index.html", {**context, **data})
    else:
        return render(request, "noticias/index.html", context)



def suscripcion(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        messages.success(request, 'Datos enviados correctamente.')
        return redirect('noticias/index.html')  # Reemplaza 'index' con el nombre de la URL de tu página de inicio

    context = {
        "categorias": categorias
    }
    return render(request, 'noticias/suscripcion.html', context)



def noticia(request, id_categoria):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id_categoria=id_categoria)
    comentario = Comentario.objects.all()
    noticia = Noticia.objects.filter(id_categoria=categoria)

    context = {
        'categoria': categoria,
        'categorias': categorias,
        'noticia': noticia,  
        'comentario': comentario,
    }
    equipo = Equipo.objects.all()
    categorias = Categoria.objects.all()
    noticia = Noticia.objects.all()
    context = {
         'equipo': equipo,
         'categorias': categorias,
         'noticia': noticia,
     }
    return render(request, 'noticias/noticia.html', context)



## GESTION DE NOTICIAS

def listado(request):
    noticia = Noticia.objects.all()
    categorias = Categoria.objects.all()
    context = {
        "noticia": noticia,
        "categorias": categorias
    }
    return render(request, 'noticias/gestion/listado.html', context)
    
from .models import Categoria

def add(request):
    formulario = NoticiaForm(request.POST or None, request.FILES or None)
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Noticia agregada exitosamente.')
        return redirect('listado')
    return render(request, "noticias/gestion/noticiasAdd.html", {"formulario": formulario, "categorias": categorias})



@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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



# api_key = 'd836e1ed4974036625c88987913d9419'
# user_input = input()

# weather_data = requests.get (
#     f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&aAPPID={api_key}' )
# if weather_data.json() ['cod'] == '404':
#     print('Ciudad no encontrada')
# else :
#     weather = weather_data.json()['weather'][0]['main']
#     temp = round(weather_data.json()['main']['temp'])
    
#     print('La temperatura  {user_input} es: {weather}')
#     print('La temperatura en {user_input} es: {temp}C')