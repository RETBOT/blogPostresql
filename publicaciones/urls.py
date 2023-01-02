# publicaciones/urls.py
from django.urls import path
from .views import (
    VistaListaPublicaciones,
    # Publicaciones
    VistaCrearPublicacion,
    VistaEditarPublicacion,
    VistaDetallePublicacion,
    VistaEliminarPublicacion,
    # Comentarios
    VisaNuevoComentarioEnPublicacion,
    )

urlpatterns = [
    path('',VistaListaPublicaciones.as_view(), name='lista_publicaciones'),
    # Publicaciones 
    path('nuevo/',VistaCrearPublicacion.as_view(), name='nueva_publicacion'),
    path('<uuid:pk>/editar/',VistaEditarPublicacion.as_view(), name='editar_publicacion'),
    path('<int:pk>/detalle/',VistaDetallePublicacion.as_view(), name='detalle_publicacion'),
    path('<int:pk>/eliminar/',VistaEliminarPublicacion.as_view(), name='eliminar_publicacion'),

    #Comentarios 
    path('comentario/publicacion/<int:pk>/', VisaNuevoComentarioEnPublicacion.as_view(), name='comenario_nuevo')
    ]    