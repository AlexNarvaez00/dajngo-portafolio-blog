from django.shortcuts import render
# Del archivo de modelos importamos el modelo "Poryect"
from .models import Project
# Create your views here.


def home (request):
    lisProjects = Project.objects.all()
    # Diccionario utilizado para pasara las variables
    # a la vista de "home.html"
    variables = {
        'lisProjects':lisProjects
    }
    return render(request,'home.html',variables)
