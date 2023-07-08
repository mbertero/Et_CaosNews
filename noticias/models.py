from django.db import models

# Create your models here.


class Usuario(models.Model):
    id_usuario       = models.AutoField(db_column='idUsuario', primary_key=True)
    contrasena       = models.CharField(max_length=20)
    nombre           = models.CharField(max_length=50)
    correo           = models.CharField(max_length=100)


class Categoria(models.Model):
    id_categoria     = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria        = models.CharField(max_length=20, blank= False, null=False)

    def __str__(self) :
        return str(self.categoria)


class Noticia(models.Model):
    id_noticia        = models.AutoField(db_column='idNoticia', primary_key=True)
    titulo            = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(blank=False, null=False)
    id_categoria      = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    img_hero          = models.ImageField(upload_to='hero', null=True, blank=True)
    bajada_titulo     = models.CharField(max_length=100)
    contenido         = models.CharField(max_length=1000)
    subtitulo         = models.CharField(max_length=100)
    img_noticias      = models.ImageField(upload_to='noticias', null=True, blank=True)
    contenido2        = models.CharField(max_length=1000)     
    subtitulo2        = models.CharField(max_length=100)
    img_noticias2     = models.ImageField(upload_to='noticias2', null=True,blank=True)
    contenido3        = models.CharField(max_length=1000)
    
    

    def __str__(self) :
        return str(self.titulo)
    
    def delete(self, using=None, keep_parents=False):
     if self.img_hero:
        self.img_hero.storage.delete(self.img_hero.name)
     if self.img_noticias:
        self.img_noticias.storage.delete(self.img_noticias.name)
     if self.img_noticias2:
        self.img_noticias2.storage.delete(self.img_noticias2.name)
     return super().delete(using, keep_parents)

    
class Equipo(models.Model):
    id_funcionario   = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre           = models.CharField(max_length=20)
    descripcion      = models.CharField(max_length=50)
    img              = models.ImageField(upload_to='img/', null=True,blank=True, verbose_name='img')
    
    
class Comentario(models.Model):
    nombre           = models.CharField(max_length=50)
    comentario       = models.CharField(max_length=100)
    img              = models.ImageField(upload_to='img/', null=True,blank=True, verbose_name='img')


    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()

    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre