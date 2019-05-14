from django.urls.conf import path
from apps.servicios.views import ObtainAuthToken, validar_Usuario, cambiar_Clave,\
    registro_Usuario, update_Usuario, registro_NN, listado_NN, update_NN,\
    delete_NN, registro_Sesion, update_Sesion, listado_Sesion,\
    listado_Areas, listado_Actividades, listado_Categorias,\
    listado_Ordenes, listado_Juegos, listado_Items,\
    registro_Calificacion_Orden, listado_Calificacion_Orden,\
    listado_Calificacion_Juego, listado_ActividadesGeneral,\
    listado_Actividades_Juegos, registro_Calificacion_Juego

app_name = 'servicios'

urlpatterns = [
    # Login
    path('api-token-auth/', ObtainAuthToken.as_view(), name='token'),
    # Validacion Usuario
    path('validarUsuario/', validar_Usuario, name='validar'),
    # Cambio clave
    path('cambiarClave/', cambiar_Clave, name='cambiar_clave'),
    # Profesor
    path('addProfesor/', registro_Usuario, name="addProfesor"),
    path('updateProfesor/<int:id>/', update_Usuario, name="updateProfesor"),
    # ALumno
    path('addAlumno/', registro_NN, name="addAlumno"),
    path('listAlumnos/<int:id>/', listado_NN, name="listAlumnos"),
    path('updateAlumno/<int:id>/', update_NN, name="updateAlumno"),
    path('deleteAlumno/<int:id>/', delete_NN, name="deleteAlumno"),
    # Sesion
    path('addSesion/', registro_Sesion, name="addSesion"),
    path('updateSesion/<int:id>/', update_Sesion, name="updateSesion"),
    path('listSesiones/<int:id>/', listado_Sesion, name="listSesiones"),
    # Area
    path('listAreas/', listado_Areas, name="listAreas"),
    # Actividades
    path('listActividades/<int:id>/', listado_Actividades, name="listActividades"),
    path('listActividadesGeneral/', listado_ActividadesGeneral, name="listActividadesGeneral"),
    # Actividad_Juego
    path('listActividadesJuego/<int:id>/', listado_Actividades_Juegos, name="listActividadesJuego"),
    # Categorias
    path('listCategorias/', listado_Categorias, name="listCategorias"),
    # Ordenes
    path('listOrdenes/<int:id_act>/<int:id_cat>/', listado_Ordenes, name="listOrdenes"),
    # Juegos
    path('listJuegos/', listado_Juegos, name="listJuegos"),
    # Items
    path('listItems/<int:id_activ>/<int:id_categ>/', listado_Items, name="listItems"),
    # Calificacion_Orden
    path('addCalificacion_Orden/', registro_Calificacion_Orden, name="addCalificacion_Orden"),
    path('listCalificacion_Orden/<int:id>/', listado_Calificacion_Orden, name="listCalificacion_Orden"),
    # Calificacion_Juego
    path('addCalificacion_Juego/', registro_Calificacion_Juego, name="addCalificacion_Orden"),
    path('listCalificacion_Juego/<int:id>/', listado_Calificacion_Juego, name="listCalificacion_Juego"),
    
]