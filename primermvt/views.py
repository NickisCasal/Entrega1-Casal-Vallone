from django.shortcuts import render
import primermvt
from primermvt.forms import Familiares_form, Animales_form, Vehiculos_form
from primermvt.models import Familiares, Animales, Vehiculos

# Create your views here.

def Inicio(request):
    return render(request, "inicio.html")

def grupofliar(request):
    if request.method == "GET":
        form = Familiares_form()
        context = {"form":form}
        return render(request, "grupofliar.html", context=context)
    else:
        form = Familiares_form(request.POST)
        if form.is_valid():
            new_familiar = Familiares.objects.create(
                name = form.cleaned_data["name"],
                edad = form.cleaned_data["edad"],
                nacimiento = form.cleaned_data["nacimiento"],
                dni = form.cleaned_data["dni"],
                active = form.cleaned_data["active"]
            )
            context = {"new_familiar":new_familiar}
        return render(request, "grupofliar.html", context=context)

def mascotas(request):
    if request.method == "GET":
        form = Animales_form()
        context = {"form":form}
        return render(request, "mascotas.html", context=context)
    else:
        form = Animales_form(request.POST)
        if form.is_valid():
            new_mascota = Animales.objects.create(
                name = form.cleaned_data["name"],
                edad = form.cleaned_data["edad"],
                tipo = form.cleaned_data["tipo"],
                raza = form.cleaned_data["raza"]
            )
            context = {"new_mascota":new_mascota}
        return render(request, "mascotas.html", context=context)

def vehiculos(request):
    if request.method == "GET":
        form = Vehiculos_form()
        context = {"form":form}
        return render(request, "vehiculos.html", context=context)
    else:
        form = Vehiculos_form(request.POST)
        if form.is_valid():
            new_vehiculo = Vehiculos.objects.create(
                name = form.cleaned_data["name"],
                precio = form.cleaned_data["precio"],
                marca = form.cleaned_data["marca"],
                patente = form.cleaned_data["patente"]
            )
            context = {"new_vehiculo":new_vehiculo}
        return render(request, "vehiculos.html", context=context)

def show_familiar(request):
    print(request.method)
    fliares = Familiares.objects.all()
    context = {'fliares':fliares}
    return render(request, 'show_familiares.html', context=context)

def show_mascota(request):
    print(request.method)
    mascotas = Animales.objects.all()
    context = {'mascotas':mascotas}
    return render(request, 'show_mascotas.html', context=context)

def show_vehiculo(request):
    print(request.method)
    vehiculos = Vehiculos.objects.all()
    context = {'vehiculos':vehiculos}
    return render(request, 'show_vehiculos.html', context=context)

def search_view(request):
    print(request.GET)
    fliares = Familiares.objects.filter(name__contains = request.GET['search'])
    context = {"fliares": fliares}
    return render(request, "search.html", context=context)