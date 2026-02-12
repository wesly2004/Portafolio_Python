from django.shortcuts import render
from .models import Proyecto

def inicio(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'web/inicio.html', {'proyectos': proyectos})
