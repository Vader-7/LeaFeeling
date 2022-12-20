from asyncore import loop
from django.contrib.auth.models import User
from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from Leaf.models import ProductoUsuario, Producto
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render


class CarritoView(UnicornView):
    user_products: QuerySetType[ProductoUsuario] = None
    user_pk: int 
    Total: int = 0
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = ProductoUsuario.objects.filter(user = self.user_pk)
        self.get_total()
    
        
    def add_producto(self, product_pk):
        item, created = ProductoUsuario.objects.get_or_create(user_id=self.user_pk, producto_id = product_pk)
        if not created:
            item.cantidad = F('cantidad') + 1
            item.save()
        self.user_products = ProductoUsuario.objects.filter(user = self.user_pk)
        self.get_total()
        
    def compra(self, product_pk):
        item = ProductoUsuario.objects.get(user_id=self.user_pk, producto_id = product_pk)
        a = Producto.objects.get(pk = product_pk)
        if item.cantidad > a.stock:
            messages.error(self.request, f"No hay suficiente {a.nombre.lower()} en stock.")
            return redirect(to = "carrito")
        else:
            a.stock = a.stock - item.cantidad
            a.save()
            item.delete()
            self.user_products = self.user_products.exclude(pk = product_pk)
            self.user_products = ProductoUsuario.objects.filter(user = self.user_pk)
            self.get_total()
            messages.success(self.request, 'Gracias por su compra.')
            return redirect(to = "carrito")
    
    def delete_item(self, product_pk):
        item = ProductoUsuario.objects.get(pk = product_pk)
        item.cantidad -= 1
        item.save()
        if item.cantidad == 0:
            item.delete()
        self.user_products = self.user_products.exclude(pk = product_pk)
        self.get_total()
        
    def delete_carrito(self, product_pk):
        item = ProductoUsuario.objects.get(pk = product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk = product_pk)
        self.get_total()
    
    def get_total(self):
        self.Total = sum(
            producto.precio_total for producto in self.user_products)