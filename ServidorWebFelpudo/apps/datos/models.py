from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NN(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70, blank=False, null=False)
    apellido = models.CharField(max_length=70, blank=False, null=False)
    fec_nacimiento = models.DateField(blank=False, null=False)
    nivel = models.CharField(max_length=50, blank=False, null=False)
    discapacidad = models.CharField(max_length=70, blank=False, null=False)

class SESION(models.Model):
    nn = models.ForeignKey(NN, on_delete=models.CASCADE)
    categoria = models.ForeignKey('areas.CATEGORIA', on_delete=models.CASCADE)
    fecha_ini = models.CharField(max_length=16, blank=False, null=False)
    fecha_fin = models.CharField(max_length=16, blank=False, null=False)
    area_visitada = models.CharField(max_length=100, blank=False, null=False)
    