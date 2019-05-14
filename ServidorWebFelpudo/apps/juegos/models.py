from django.db import models
from apps.areas.models import ACTIVIDAD, CATEGORIA
from apps.datos.models import SESION
# Create your models here.
class JUEGO(models.Model):
    nombre = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return self.nombre

class ACTIVIDAD_JUEGO(models.Model):
    actividad = models.ForeignKey(ACTIVIDAD, on_delete=models.CASCADE)
    juego = models.ForeignKey(JUEGO, on_delete=models.CASCADE)
    nombre = models.TextField(blank=False, null=False)
    
    
    def __str__(self):
        return self.nombre       

class ITEM(models.Model):
    actividad_juego =  models.ForeignKey(ACTIVIDAD_JUEGO, on_delete=models.CASCADE)
    categoria  =  models.ForeignKey(CATEGORIA, on_delete=models.CASCADE)
    texto = models.TextField(blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.texto
    
class CALIFICACION_JUEGO(models.Model):
    actividad_juego =  models.ForeignKey(ACTIVIDAD_JUEGO, on_delete=models.CASCADE)
    sesion =  models.ForeignKey(SESION, on_delete=models.CASCADE)
    indicador = models.CharField(max_length=70, blank=False, null=False)