from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad',  'tipo']
    
    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor[0] == 'L':
            raise forms.ValidationError("La primera letra de la ciudad no puede ser 'L' ")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if len(valor) > 10000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 10000")
        return valor
    
    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if len(valor) == 0 and len(valor) > 7 :
            raise forms.ValidationError("Ingrese un numero de cuarto diferente a 0 y menor a 7")
        return valor
    
    def clean_nombre_propietario(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese un nombre y dos apellidos")
        return valor


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']
    
    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if len(valor) > 10000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 10000")
        return valor
    
    def clean_numero_cuartos(self):
        valor = self.cleaned_data['numero_cuartos']
        if len(valor) == 0 and len(valor) > 7 :
            raise forms.ValidationError("Ingrese un numero de cuarto diferente a 0 y menor a 7")
        return valor
    
    def clean_nombre_propietario(self):
        valor = self.cleaned_data['nombre_propietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese un nombre y dos apellidos")
        return valor


