# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.juegos.models import JUEGO, ITEM, CALIFICACION_JUEGO,\
    ACTIVIDAD_JUEGO

# Register your models here.
admin.site.register(JUEGO)
admin.site.register(ITEM)
admin.site.register(CALIFICACION_JUEGO)
admin.site.register(ACTIVIDAD_JUEGO)