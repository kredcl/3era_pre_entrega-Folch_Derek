
from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'edad']


class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ['nombre', 'apellido', 'email', 'restorant']
    

class restoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    email = forms.EmailField()



   