from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Operador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre