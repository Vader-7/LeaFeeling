from django.db import models
from pyparsing import NoMatch
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=51)
    descripcion = models.TextField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to="productos/", null=True)
    
    def __str__(self):
        return self.nombre
    
    
opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    

class ProductoUsuario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default = 1)
    agregar = models.DateTimeField(auto_now_add=True)
    
    @property
    def precio_total(self):
        return self.cantidad * self.producto.precio
    
    def __str__(self):
        return self.producto.nombre
