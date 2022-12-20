from dataclasses import fields
from .models import Producto, Contacto
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
        

class CustomUserCreationForm(UserCreationForm):
    pass