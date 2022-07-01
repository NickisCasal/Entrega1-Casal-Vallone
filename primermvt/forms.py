from email.policy import default
from django import forms
from primermvt.models import Animales, Vehiculos

class Familiares_form(forms.Form):
    name = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    nacimiento = forms.CharField(max_length=10)
    dni = forms.IntegerField()
    active = forms.BooleanField()

class Animales_form(forms.ModelForm):
    class Meta:
        model = Animales
        fields = "__all__"


class Vehiculos_form(forms.ModelForm):
    class Meta:
        model = Vehiculos
        fields = "__all__"