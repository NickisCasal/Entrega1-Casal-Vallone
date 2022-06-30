from django.contrib import admin

from primermvt.models import Familiares, Animales, Vehiculos
# Register your models here.

@admin.register(Familiares)
class FamiliaresAdmin(admin.ModelAdmin):
    list_display = ["name", "edad", "nacimiento", "dni"]


@admin.register(Animales)
class AnimalesAdmin(admin.ModelAdmin):
    list_display = ["name", "edad", "tipo", "raza"]


@admin.register(Vehiculos)
class VehiculosAdmin(admin.ModelAdmin):
    list_display = ["name", "precio", "marca", "patente"]