from django.db import models

class Producto(models.Model):
    referencia = models.CharField(max_length=30, null=False, blank=False)
    codigo = models.CharField(max_length=30, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    precio = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        
        return self.nombre
    

class ExcelFile(models.Model):
    archivo = models.FileField(upload_to='archivos_excel/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
