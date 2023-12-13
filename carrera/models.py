from django.db import models
from instituto.models import Instituto

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()
    cantidad_materias = models.IntegerField()
    instituto = models.ForeignKey(Instituto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
