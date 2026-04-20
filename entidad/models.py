from django.db import models


class Ropa(models.Model):
    marca = models.CharField(max_length=50)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)
    lisa = models.BooleanField(default=False)
    genero = models.IntegerField()
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre