
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('noticia/<id_categoria>/', views.noticia, name= 'noticia'),
    path('listado', views.listado , name='listado'),
    path('add', views.add, name='add'),
    path('edit/<id_noticia>' , views.edit , name='edit'),
    path('delete/<id_noticia>', views.delete , name='delete'),
    path('suscripcion', views.suscripcion, name='suscripcion'),
    
    path('salir', views.salir , name='salir'),
    path('login', views.login, name='login'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
