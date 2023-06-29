#CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia 
        fields = ['titulo', 'fecha_publicacion', 'id_categoria', 'img_hero', 
                  'bajada_titulo', 'contenido', 'subtitulo', 'img_noticias', 'contenido2',
                   'subtitulo2','img_noticias2', 'contenido3'] 
   
       
        # fields = '__all__' 

