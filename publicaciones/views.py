#publicaciones/views.py
# by: RETBOT
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Publicacion, Comentario
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
# Create your views here.
class VistaListaPublicaciones(ListView):
  model = Publicacion
  template_name = 'lista_publicaciones.html'

  
## Publicaciones
class VistaCrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'nueva_publicacion.html'
    fields = ['titulo', 'cuerpo','imagen']

    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
# by: RETBOT
class VistaDetallePublicacion(DetailView):
  model = Publicacion
  template_name = 'detalle_publicacion.html'
  context_object_name = 'pub'
  
class VistaEditarPublicacion(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    template_name = 'editar_publicacion.html'
    fields = ['titulo', 'cuerpo','imagen',]
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user
    # by: RETBOT
class VistaEliminarPublicacion(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacion
    template_name = 'eliminar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user
    

# Comentarios
class VisaNuevoComentarioEnPublicacion(CreateView):
    model = Comentario
    template_name = 'comentario_nuevo.html'
    context_object_name = 'comen'
    fields = ['titulo','comentario',]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
# by: RETBOT
