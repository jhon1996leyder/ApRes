from django.db import models

class Productos(models.Model):
    referencias=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    fechaIngreso=models.DateTimeField(auto_now_add=True)
