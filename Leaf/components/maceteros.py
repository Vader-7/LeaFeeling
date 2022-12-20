from django.contrib.auth.models import User
from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from Leaf.models import ProductoUsuario, Producto


class MaceterosView(UnicornView):
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
    
    
    def delete_item(self, product_pk):
        item = ProductoUsuario.objects.filter(pk = product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk = product_pk)
        self.get_total()
    
    
    def get_total(self):
        self.Total = sum(
            producto.precio_total for producto in self.user_products)