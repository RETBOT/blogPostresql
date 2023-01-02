# blog/urls.py 
from django.urls import path
from .views import VistaPaginaInicio 
   # by: RETBOT
urlpatterns = [ 
  path('', VistaPaginaInicio.as_view(), name='inicio'),
] # by: RETBOT
