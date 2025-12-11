from django.db import models

# Clase Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    pais_origen = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

# Clase Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre

# Clase Celular
class Celular(models.Model):
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    # FK
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"
