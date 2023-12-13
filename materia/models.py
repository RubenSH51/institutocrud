from django.db import models
from carrera.models import Carrera

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
