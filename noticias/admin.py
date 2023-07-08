from django.contrib import admin
from .models import Noticia, Categoria, Equipo, Comentario, Ciudad
# Register your models here.

admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Equipo)
admin.site.register(Comentario)
admin.site.register(Ciudad)