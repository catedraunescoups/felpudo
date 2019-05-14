from rest_framework import serializers
from django.contrib.auth.models import User
from apps.datos.models import NN, SESION
from tesis.settings import DATE_INPUT_FORMATS

from datetime import datetime
from apps.areas.models import AREA, ACTIVIDAD, CATEGORIA, ORDEN,\
    CALIFICACION_ORDEN
from apps.juegos.models import JUEGO, ITEM, CALIFICACION_JUEGO, ACTIVIDAD_JUEGO

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
     
    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validate_data):
        instance.first_name = validate_data['first_name']
        instance.last_name = validate_data['last_name']
        instance.email = validate_data['email']
        instance.save()
        return instance

class NNSerializer(serializers.ModelSerializer):
    fec_nacimiento = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    
    class Meta:
        model = NN
        fields = ('id', 'nombre', 'apellido', 'fec_nacimiento', 'nivel', 'discapacidad','usuario')
        
        """def create(self, validated_data):
            datos_obj = NNA(**validated_data)
            datos_obj.save()
            return datos_obj
        
        
        def update(self, instance, validated_data):
            instance.nombre = validated_data['nombre']
            instance.apellido = validated_data['apellido']
            instance.fec_nacimiento = validated_data['fec_nacimiento']
            instance.grado = validated_data['grado']
            instance.usuario = validated_data['usuario']
            instance.save()
            return instance"""
            
class SesionSerializer(serializers.ModelSerializer):
    fecha_ini = serializers.CharField(required=False)
    fecha_fin = serializers.CharField(required=False)
    area_visitada = serializers.CharField(required=False)
    
    def create(self, validated_data):
        sesion = SESION(**validated_data)
        sesion.fecha_ini = datetime.now().strftime("%d-%m-%Y %H:%M")
        sesion.fecha_fin = datetime.now().strftime("%d-%m-%Y %H:%M")
        sesion.area_visitada = "Ninguna"
        sesion.save()
        return sesion

    def update(self, instance, validated_data):
        instance.fecha_fin = datetime.now().strftime("%d-%m-%Y %H:%M")
        instance.area_visitada = validated_data['area_visitada']
        instance.save()
        return instance
    
    class Meta:
        model = SESION
        fields = ('id', 'fecha_ini', 'fecha_fin', 'area_visitada', 'nn','categoria')
        
class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AREA
        fields = ('id', 'nombre', 'referencia')
        
class ActividadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ACTIVIDAD
        fields = ('id', 'nombre', 'area', 'referencia')

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CATEGORIA
        fields = ('id', 'nombre')

class OrdenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ORDEN
        fields = ('id', 'texto', 'codigo', 'estado')
        #fields = ('id', 'nombre', 'texto', 'estado', 'actividad', 'categoria')

class Calificacion_OrdenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CALIFICACION_ORDEN
        fields = ('id', 'indicador', 'orden', 'sesion')

class JuegoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JUEGO
        fields = ('id', 'nombre') 
        
class Actividad_JuegoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ACTIVIDAD_JUEGO
        fields = ('id', 'nombre')

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ITEM
        fields = ('texto', 'codigo') 
              
class Calificacion_JuegoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CALIFICACION_JUEGO
        fields = ('id', 'indicador','actividad_juego','sesion')
        