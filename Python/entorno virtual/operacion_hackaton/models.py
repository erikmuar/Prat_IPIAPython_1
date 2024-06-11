from django.db import models

class MiUser(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=50)
    edad = models.IntegerField()
    es_admin = models.BooleanField(default=False)
    