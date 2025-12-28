from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='blog_imagenes/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)