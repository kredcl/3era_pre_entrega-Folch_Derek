from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
     return self.nombre

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    restorant = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class resto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
   
    def __str__(self):
     return self.nombre
