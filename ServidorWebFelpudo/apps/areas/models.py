from django.db import models
from apps.datos.models import SESION

# Create your models here.
class AREA(models.Model):
    nombre = models.CharField(max_length=70, blank=False, null=False)
    referencia = models.CharField(max_length=70, blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    
class ACTIVIDAD(models.Model):
    area = models.ForeignKey(AREA, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, blank=False, null=False)
    referencia = models.CharField(max_length=70, blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    
class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=70, blank=False, null=False)
    
    def __str__(self):
        return self.nombre

class ORDEN(models.Model):
    texto = models.TextField(blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)
    estado = models.IntegerField()
    actividad = models.ForeignKey(ACTIVIDAD, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CATEGORIA, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.texto

class CALIFICACION_ORDEN(models.Model):
    sesion = models.ForeignKey(SESION, on_delete=models.CASCADE)
    orden = models.ForeignKey(ORDEN, on_delete=models.CASCADE)
    indicador = models.CharField(max_length=70, blank=False, null=False)