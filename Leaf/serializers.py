from asyncore import read
from dataclasses import fields
from .models import Producto, Categoria, ProductoUsuario
from rest_framework import serializers
from django.contrib.auth import authenticate, login

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    
class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source='categoria.nombre')
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class ProductoUsuarioSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.CharField(read_only=True, source='producto.nombre')
    producto = CategoriaSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='producto')
    class Meta:
        model = ProductoUsuario
        fields = '__all__'