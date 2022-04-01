from datetime import datetime
from django.db import models

# Create your models here.
class Post(models.Model):
    # Declaranmos los campos que tendra nuestra tabla en la 
    # base de datos.
    title = models.CharField(max_length=150)
    descripcion = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    fecha = models.DateField(datetime.today)