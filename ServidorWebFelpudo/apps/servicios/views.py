from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, parsers, renderers
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from apps.servicios.serializers import UsuarioSerializer, NNSerializer,\
    SesionSerializer, ActividadSerializer,\
    CategoriaSerializer, OrdenSerializer, JuegoSerializer, ItemSerializer,\
    Calificacion_OrdenSerializer, Calificacion_JuegoSerializer, AreaSerializer,\
    Actividad_JuegoSerializer
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from apps.datos.models import NN, SESION
from apps.areas.models import AREA, ACTIVIDAD, CATEGORIA, ORDEN,\
    CALIFICACION_ORDEN
from apps.juegos.models import JUEGO, ITEM, CALIFICACION_JUEGO, ACTIVIDAD_JUEGO


# Create your views here.
####### Servicios Web #######

### RECUPERAR PASSWORD ###
### VALIDA USUARIO POR CORREO
@api_view(['POST'])
def validar_Usuario(request):
    response = ""
    try:
        correo = request.data["correo"]
        user = User.objects.get(email=correo)
        if (user != None):
            response = "yes"
        else:
            response = "no"
    except User.DoesNotExist:
        response = "no"
    
    return Response({'response': response})

### CAMBIA LA CLAVE
@api_view(['POST'])
def cambiar_Clave(request):
    response = ""
    try:
        correo = request.data["correo"]
        password = request.data["password"]
        user = User.objects.get(email__exact=correo)
        user.set_password(password)
        user.save()
        response = "yes"
    except User.DoesNotExist:
        response = "no"
    
    return Response({'response': response})

### OBTENER TOKEN ###
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token = Token()
        token.key, token.created  = None, None
                
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'id' : user.id, 'name' : user.first_name + " " + user.last_name })

### REGISTRO DE USUARIO ###
@api_view(['POST'])
def registro_Usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            Token.objects.create(user=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
### UPDATE Y DELETE USUARIO
@api_view(['GET', 'POST', 'DELETE'])
def update_Usuario(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    
### REGISTRO DE NN ###
@api_view(['POST'])
def registro_NN(request):
    if request.method == 'POST':
        serializer = NNSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### UPDATE NNA
@api_view(['GET', 'POST'])
def update_NN(request, id):
    try:
        nn = NN.objects.get(id=id)
    except NN.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NNSerializer(nn)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NNSerializer(nn, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
 
### DELETE NNA
@api_view(['POST'])
def delete_NN(request, id):
    try:
        nn = NN.objects.get(id=id)
    except NN.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        response = ""
        if nn.delete():
            response = "yes"
        else:
            response = "no"
        
        return Response({'deleted': response})

@api_view(['GET'])
def listado_NN(request, id):
    #muestra los NNA de un solo profesor
    if request.method == 'GET':
        nna = NN.objects.filter(usuario=id)
        serializer = NNSerializer(nna, many=True)
        return Response(serializer.data)
   
@api_view(['GET', 'POST'])
def registro_Sesion(request):
    
    if request.method == 'GET':
        sesion = SESION.objects.filter(nn=id)
        serializer = SesionSerializer(sesion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### UPDATE SESION
@api_view(['POST'])
def update_Sesion(request, id):
    try:
        sesion = SESION.objects.get(id=id)
    except SESION.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SesionSerializer(sesion, data=data)
        if serializer.is_valid():
            serializer.update(sesion, serializer.validated_data)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def listado_Sesion(request, id):
    #Lista las sesiones de un NNA
    if request.method == 'GET':
        sesion = SESION.objects.filter(persona=id)
        serializer = SesionSerializer(sesion, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def listado_Areas(request):
    #Lista todas las areas
    if request.method == 'GET':
        area = AREA.objects.all()
        serializer = AreaSerializer(area, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listado_Actividades(request, id):
    #Lista las actividades de una area
    if request.method == 'GET':
        area = ACTIVIDAD.objects.filter(area=id)
        serializer = ActividadSerializer(area, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listado_ActividadesGeneral(request):
    if request.method == 'GET':
        actividad = ACTIVIDAD.objects.all().order_by('referencia')
        serializer = ActividadSerializer(actividad, many=True)
        return Response(serializer.data)   

@api_view(['GET'])
def listado_Categorias(request):
    #Lista las categorias
    if request.method == 'GET':
        categoria = CATEGORIA.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listado_Ordenes(request, id_act, id_cat):
    #Lista las ordenes por categoria
    if request.method == 'GET':
        orden = ORDEN.objects.filter(actividad=id_act, categoria=id_cat).order_by('estado')
        serializer = OrdenSerializer(orden, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def listado_Juegos(request):
    #Lista todos los juegos
    if request.method == 'GET':
        juego = JUEGO.objects.all()
        serializer = JuegoSerializer(juego, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listado_Actividades_Juegos(request, id):
    #Lista los juegos por actividad
    if request.method == 'GET':
        actividad_juego = ACTIVIDAD_JUEGO.objects.filter(actividad=id)
        serializer = Actividad_JuegoSerializer(actividad_juego, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def listado_Items(request, id_activ, id_categ):
    #Lista las item por juego
    if request.method == 'GET':
        item = ITEM.objects.filter(actividad_juego=id_activ, categoria=id_categ )
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def registro_Calificacion_Orden(request):
    
    if request.method == 'GET':
        calificacion = CALIFICACION_ORDEN.objects.filter(orden=id)
        serializer = Calificacion_OrdenSerializer(calificacion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Calificacion_OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listado_Calificacion_Orden(request, id):
    #Lista las calificaciones de un orden
    if request.method == 'GET':
        calificacion = CALIFICACION_ORDEN.objects.filter(orden=id)
        serializer = Calificacion_OrdenSerializer(calificacion, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def registro_Calificacion_Juego(request):
    
    if request.method == 'GET':
        calificacionj = CALIFICACION_JUEGO.objects.filter(orden=id)
        serializer = Calificacion_JuegoSerializer(calificacionj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Calificacion_JuegoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listado_Calificacion_Juego(request, id):
    #Lista las calificaciones de un orden
    if request.method == 'GET':
        calificacionj = CALIFICACION_JUEGO.objects.filter(orden=id)
        serializer = Calificacion_JuegoSerializer(calificacionj, many=True)
        return Response(serializer.data)
