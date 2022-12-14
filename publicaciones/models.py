#publicaciones/models.py
# by: RETBOT
from django.db import models 
from django.contrib.auth import get_user_model
from django.urls import reverse
# by: RETBOT
class Publicacion(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
  cuerpo = models.TextField()
  imagen = models.ImageField(upload_to="img_pub", null=True)

  def __str__(self):
    return self.titulo
  
  def get_absolute_url(self):
    return reverse('detalle_publicacion',args=[str(self.id)])
  # by: RETBOT
class Comentario(models.Model):
  titulo = models.ForeignKey(
      Publicacion, 
      on_delete=models.CASCADE,
      related_name='comentarios',
  )
  
  autor = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
  )

  comentario = models.TextField()

  def __str__(self):
    return self.comentario
    # by: RETBOT
  def get_absolute_url(self):
    return reverse("lista_publicaciones")
  # by: RETBOT
