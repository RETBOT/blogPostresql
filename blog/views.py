# blog/views.py 
from django.views.generic import TemplateView

class VistaPaginaInicio(TemplateView): 
  template_name = 'inicio.html'