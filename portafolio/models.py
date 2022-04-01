from django.db import models

# Importamos los tipos de datos que soporta la base de datos
# estos titpos de datos hacen referencia a los tipos de datos dde las
# columnas de la tabla
from django.db.models.fields import CharField
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

# Create your models here.

# Primera clase que servira como modelo
# en la base de datos.


class Project(models.Model):
    # Ttitulo del proyecto.
    title = CharField(max_length=100)
    # Descripcion del proyecto.
    description = CharField(max_length=250)
    # Imagen del proyecto.
    img = ImageField(upload_to="portafolio/img")
    # URL del proyecto
    url = URLField(blank=True)
