from dataclasses import dataclass
import datetime
from pickletools import read_unicodestring1
from tokenize import group
from django.http import Http404
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, ProductoUsuario, Contacto, Categoria
from django.contrib.auth.models import User
from .forms import ProductoForm, ContactoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets, authentication, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProductoSerializer, CategoriaSerializer, ProductoUsuarioSerializer


# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser,]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUser,]
    
    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productos = productos.filter(nombre_contains = nombre)
            
        return productos

class ProductoUsuarioViewset(viewsets.ModelViewSet):
    queryset = ProductoUsuario.objects.all()
    serializer_class = ProductoUsuarioSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        productosusuarios = ProductoUsuario.objects.all()
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productosusuarios = productosusuarios.filter(nombre_contains = nombre)
            
        return productosusuarios



# Create your views here.
@permission_required('Leaf.delete_producto')
def delProducto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "PRODUCTO ELIMINADO.")
    return redirect(to = "administracion")


@login_required
def tarjeta(request):
    return render(request, 'Leaf/tarjeta.html')
    
    
def home(request):
    return render(request, 'Leaf/home.html')

def nosotros(request):
    return render(request, 'Leaf/nosotros.html')

@login_required
def carrito(request):
    Productos = Producto.objects.all()
    data = {"Productos": Productos}
    return render(request, 'Leaf/carrito.html', data)

@login_required
def seguimiento(request):
    return render(request, 'Leaf/seguimiento.html')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            my_group = Group.objects.get(name='cliente') 
            my_group.user_set.add(user)
            messages.success(request, f"BIENVENIDO A LEAFEELING {user.username.upper()}")
            return redirect(to = "home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def semillas(request):
    Productos = Producto.objects.all()
    data = {"Productos": Productos}
    return render(request, 'Leaf/semillas.html', data)

def maceteros(request):
    Productos = Producto.objects.all()
    data = {"Productos": Productos}
    return render(request, 'Leaf/maceteros.html', data)

def fertilizantes(request):
    Productos = Producto.objects.all()
    data = {"Productos": Productos}
    return render(request, 'Leaf/fertilizantes.html', data)


@permission_required('Leaf.view_producto')
def administracion(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {"entity": productos,
            "paginator": paginator
        }
    return render(request, 'Leaf/administracion.html', data)


@permission_required('Leaf.change_producto')
def modificar(request, id):
    Productos = get_object_or_404(Producto, id = id)
    data = {"Form": ProductoForm(instance=Productos)}
    if request.method == "POST":
        formulario = ProductoForm(
            data=request.POST, instance=Productos, files=request.FILES
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "PRODUCTO MODIFICADO.")
            return redirect(to = "administracion")
        data["Form"] = formulario
    return render(request, 'Leaf/modificar.html', data)

@login_required
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "MENSAJE ENVIADO.")
            return redirect(to = "/")
        else:
            data["form"] = formulario
    return render(request, 'Leaf/contacto.html', data)


@permission_required('Leaf.add_producto')
def addProducto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "PRODUCTO AGREGADO.")
        else:
            data["form"] = formulario
    return render(request, 'Leaf/add.html', data)








