from django.db import models

# Create your models here.

class Conocimiento(models.Model):
    #Imagenes
    imagen = models.ImageField(upload_to='images/')
    #Resumen
    resumen = models.CharField(max_length=200)

    def __str__(self):
        return self.resumen