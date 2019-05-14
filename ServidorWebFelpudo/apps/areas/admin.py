# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.areas.models import AREA, ACTIVIDAD, CATEGORIA, ORDEN,\
    CALIFICACION_ORDEN

# Register your models here.
admin.site.register(AREA)
admin.site.register(ACTIVIDAD)
admin.site.register(CATEGORIA)
admin.site.register(ORDEN)
admin.site.register(CALIFICACION_ORDEN)