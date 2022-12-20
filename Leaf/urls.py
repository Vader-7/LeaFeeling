from unicodedata import name
from django.urls import path, include
from .views import CategoriaViewSet, ProductoViewset, ProductoUsuarioViewset, delProducto, home, nosotros, login, seguimiento, registro, semillas, maceteros, fertilizantes, administracion, carrito, modificar, contacto, addProducto, delProducto, tarjeta
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('productousuario', ProductoUsuarioViewset)
router.register('categoria', CategoriaViewSet)

urlpatterns = [
    path('', home,name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('login/', login, name="login"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('registro/', registro, name="registro"),
    path('semillas/', semillas, name="semillas"),
    path('maceteros/', maceteros, name="maceteros"),
    path('fertilizantes/', fertilizantes, name="fertilizantes"),
    path('administracion/', administracion, name="administracion"),
    path('carrito/', carrito, name="carrito"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('contacto/', contacto, name="contacto"),
    path('addproducto/', addProducto, name="addproducto"),
    path('delproducto/<id>/', delProducto, name="delproducto"),
    path('api/', include(router.urls)),
    path('tarjeta/', tarjeta, name="tarjeta")
]
