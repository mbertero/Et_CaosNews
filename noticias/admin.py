from django.contrib import admin
from .models import Noticia, Categoria, Equipo, Comentario
# Register your models here.

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Comentario)