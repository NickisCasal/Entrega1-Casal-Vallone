from winreg import DeleteValue
from django.shortcuts import render
from primermvt.forms import Familiares_form, Animales_form, Vehiculos_form
from primermvt.models import Familiares, Animales, Vehiculos
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
# Create your views here.

def Inicio(request):
    return render(request, "inicio.html")

# def grupofliar(request):
#     if request.method == "GET":
#         form = Familiares_form()
#         context = {"form":form}
#         return render(request, "grupofliar.html", context=context)
#     else:
#         form = Familiares_form(request.POST)
#         if form.is_valid():
#             new_familiar = Familiares.objects.create(
#                 name = form.cleaned_data["name"],
#                 edad = form.cleaned_data["edad"],
#                 nacimiento = form.cleaned_data["nacimiento"],
#                 dni = form.cleaned_data["dni"],
#                 active = form.cleaned_data["active"]
#             )
#             context = {"new_familiar":new_familiar}
#         return render(request, "grupofliar.html", context=context)

class crear_familiar(CreateView):
    model = Familiares
    template_name = "grupofliar.html"
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail_familiar", kwargs={"pk":self.object.pk})
        

# def mascotas(request):
#     if request.method == "GET":
#         form = Animales_form()
#         context = {"form":form}
#         return render(request, "mascotas.html", context=context)
#     else:
#         form = Animales_form(request.POST)
#         if form.is_valid():
#             new_mascota = Animales.objects.create(
#                 name = form.cleaned_data["name"],
#                 edad = form.cleaned_data["edad"],
#                 tipo = form.cleaned_data["tipo"],
#                 raza = form.cleaned_data["raza"]
#             )
#             context = {"new_mascota":new_mascota}
#         return render(request, "mascotas.html", context=context)

class crear_mascota(CreateView):
    model = Animales
    template_name = "mascotas.html"
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail_mascota", kwargs={"pk":self.object.pk})

# def vehiculos(request):
#     if request.method == "GET":
#         form = Vehiculos_form()
#         context = {"form":form}
#         return render(request, "vehiculos.html", context=context)
#     else:
#         form = Vehiculos_form(request.POST)
#         if form.is_valid():
#             new_vehiculo = Vehiculos.objects.create(
#                 name = form.cleaned_data["name"],
#                 precio = form.cleaned_data["precio"],
#                 marca = form.cleaned_data["marca"],
#                 patente = form.cleaned_data["patente"]
#             )
#             context = {"new_vehiculo":new_vehiculo}
#         return render(request, "vehiculos.html", context=context)

class crear_vehiculo(CreateView):
    model = Vehiculos
    template_name = "vehiculos.html"
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail_vehiculo", kwargs={"pk":self.object.pk})

def show_familiar(request):
    fliares = Familiares.objects.all()
    context = {'fliares':fliares}
    return render(request, 'show_familiares.html', context=context)


def detail_familiar(request, pk):
    try:
        fliar = Familiares.objects.get(id=pk)
        context = {"fliar": fliar}
        return render(request, "familiar_detalle.html", context=context)
    except:
        context = {"error":"El familiar no existe"}
        return render(request, "show_familiares.html", context=context)

def eliminar_familiar(request, pk):
    try:
        if request.method == "GET":
            fliar = Familiares.objects.get(id=pk)
            context = {"fliar": fliar}
        else:
            fliar = Familiares.objects.get(id=pk)
            fliar.delete()
            context = {"message": "El familiar se eliminó correctamente"}
        return render(request, "eliminar_familiar.html", context=context)
    except:
        context = {"message": "El Familiar no existe"}
        return render(request, "eliminar_familiar.html", context=context)

class editar_familiar(UpdateView):
    model = Familiares 
    template_name = "editar_familiar.html"
    fields = ["name", "nacimiento"]

    def get_success_url(self):
        return reverse("detail_familiar", kwargs={"pk":self.object.pk})



def show_mascota(request):
    print(request.method)
    mascotas = Animales.objects.all()
    context = {'mascotas':mascotas}
    return render(request, 'show_mascotas.html', context=context)

def detail_mascota(request, pk):
    try:
        mascota = Animales.objects.get(id=pk)
        context = {"mascota": mascota}
        return render(request, "mascota_detalle.html", context=context)
    except:
        context = {"error":"La mascota no existe"}
        return render(request, "show_mascotas.html", context=context)

def eliminar_mascota(request, pk):
    try:
        if request.method == "GET":
            mascota = Animales.objects.get(id=pk)
            context = {"mascota": mascota}
        else:
            mascota = Animales.objects.get(id=pk)
            mascota.delete()
            context = {"message": "La mascota se eliminó correctamente"}
        return render(request, "eliminar_mascota.html", context=context)
    except:
        context = {"message": "El Familiar no existe"}
        return render(request, "eliminar_mascota.html", context=context)

class editar_mascota(UpdateView):
    model = Animales 
    template_name = "editar_mascota.html"
    fields = ["name", "edad"]

    def get_success_url(self):
        return reverse("detail_mascota", kwargs={"pk":self.object.pk})

def show_vehiculo(request):
    print(request.method)
    vehiculos = Vehiculos.objects.all()
    context = {'vehiculos':vehiculos}
    return render(request, 'show_vehiculos.html', context=context)

def detail_vehiculo(request, pk):
    try:
        vehiculo = Vehiculos.objects.get(id=pk)
        context = {"vehiculo": vehiculo}
        return render(request, "vehiculo_detalle.html", context=context)
    except:
        context = {"error":"El vehiculo no existe"}
        return render(request, "show_vehiculos.html", context=context)

def eliminar_vehiculo(request, pk):
    try:
        if request.method == "GET":
            vehiculo = Vehiculos.objects.get(id=pk)
            context = {"vehiculo": vehiculo}
        else:
            vehiculo = Vehiculos.objects.get(id=pk)
            vehiculo.delete()
            context = {"message": "El vehículo se eliminó correctamente"}
        return render(request, "eliminar_vehiculo.html", context=context)
    except:
        context = {"message": "El vehículo no existe"}
        return render(request, "eliminar_vehículo.html", context=context)

class editar_vehiculo(UpdateView):
    model = Vehiculos 
    template_name = "editar_vehiculo.html"
    fields = ["name", "precio"]

    def get_success_url(self):
        return reverse("detail_vehiculo", kwargs={"pk":self.object.pk})

def search_view(request):
    print(request.GET)
    fliares = Familiares.objects.filter(name__contains = request.GET['search'])
    context = {"fliares": fliares}
    return render(request, "search.html", context=context)