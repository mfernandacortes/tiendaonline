from django.db import models


class Ropa(models.Model):
    marca = models.CharField(max_length=50)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)
    lisa = models.BooleanField()
    genero = models.IntegerField()
    
