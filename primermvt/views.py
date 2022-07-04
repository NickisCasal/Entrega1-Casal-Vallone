from multiprocessing import AuthenticationError
from winreg import DeleteValue
from django.shortcuts import render, redirect
from primermvt.forms import Familiares_form, Animales_form, Vehiculos_form
from primermvt.models import Familiares, Animales, Vehiculos
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from entregablemvt.forms import User_registration_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):

    if request.method == "POST":
        form =AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {"mensaje": f"¡¡Bienvenido {username}!!"}
                return render(request, "inicio.html", context=context)
            else:
                context = {"error": "No existe el usuario"}
                form = AuthenticationForm()
                return render(request, "auth/login.html", context=context)
        else:
            errors = form.errors
            context = {"errors":form.errors, "form":form}
            form = AuthenticationForm()
            return render(request, "auth/login.html", context=context)
                

    else:
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "auth/login.html", context=context)

def logout_view(request):
    logout(request)
    context = {"deslogueado":"deslogueado correctamente"}
    return render(request, "inicio.html", context=context)

def Inicio(request):
    return render(request, "inicio.html")
def contacto(request):
    return render(request, "contacto.html")

def register_view(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            context={"mensaje": f"Usuario creado correctamente, ¡Bienvenido {username}!"}
            return render(request, "inicio.html", context=context)
        else:
            errors = form.errors
            form = User_registration_form()
            context= {"errors":errors, "form":form}
            return render(request, "auth/register.html", context=context)
    else:
        form = User_registration_form()
        context = {"form":form}
        return render(request, "auth/register.html", context=context)


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

class crear_familiar(LoginRequiredMixin, CreateView):
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

class crear_mascota(LoginRequiredMixin, CreateView):
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

class crear_vehiculo(LoginRequiredMixin, CreateView):
    model = Vehiculos
    template_name = "vehiculos.html"
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail_vehiculo", kwargs={"pk":self.object.pk})

def show_familiar(request):
    if request.user.is_authenticated:
        fliares = Familiares.objects.all()
        context = {'fliares':fliares}
        return render(request, 'show_familiares.html', context=context)

    else:
        return redirect("login")


def detail_familiar(request, pk):
    try:
        if request.user.is_authenticated:
            fliar = Familiares.objects.get(id=pk)
            context = {"fliar": fliar}
            return render(request, "familiar_detalle.html", context=context)
        else:
            return redirect("login")
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

class editar_familiar(LoginRequiredMixin, UpdateView):
    model = Familiares 
    template_name = "editar_familiar.html"
    fields = ["name", "nacimiento"]

    def get_success_url(self):
        return reverse("detail_familiar", kwargs={"pk":self.object.pk})



def show_mascota(request):
    if request.user.is_authenticated:
        mascotas = Animales.objects.all()
        context = {'mascotas':mascotas}
        return render(request, 'show_mascotas.html', context=context)
    else:
        return redirect("login")

def detail_mascota(request, pk):
    try:
        if request.user.is_authenticated:
            mascota = Animales.objects.get(id=pk)
            context = {"mascota": mascota}
            return render(request, "mascota_detalle.html", context=context)
        else:
            return redirect("login")
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

class editar_mascota(LoginRequiredMixin, UpdateView):
    model = Animales 
    template_name = "editar_mascota.html"
    fields = ["name", "edad"]

    def get_success_url(self):
        return reverse("detail_mascota", kwargs={"pk":self.object.pk})

def show_vehiculo(request):
    if request.user.is_authenticated:
        vehiculos = Vehiculos.objects.all()
        context = {'vehiculos':vehiculos}
        return render(request, 'show_vehiculos.html', context=context)
    else:
        return redirect("login")

def detail_vehiculo(request, pk):
    try:
        if request.user.is_authenticated:
            vehiculo = Vehiculos.objects.get(id=pk)
            context = {"vehiculo": vehiculo}
            return render(request, "vehiculo_detalle.html", context=context)
        else:
            return redirect("login")
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

class editar_vehiculo(LoginRequiredMixin, UpdateView):
    model = Vehiculos 
    template_name = "editar_vehiculo.html"
    fields = ["name", "precio"]

    def get_success_url(self):
        return reverse("detail_vehiculo", kwargs={"pk":self.object.pk})

def search_view(request):
    if request.method == "GET":
        fliares = Familiares.objects.filter(name__contains = request.GET['search'])
        mascotas = Animales.objects.filter(name__contains = request.GET['search'])
        vehiculos = Vehiculos.objects.filter(name__contains = request.GET['search'])
        context = {"fliares": fliares, "mascotas": mascotas, "vehiculos": vehiculos}
        return render(request, "search.html", context=context)
    else:
        context = {"message": "No se encontró nada"}
        return render(request, "inicio.html", context=context)


# @login_required
# def editarperfil(request):
#     usuario = request.user
#     if request.method == "POST":
#         miFormulario = User_registration_form(request.POST)
#         if miFormulario.is_valid:
#             informacion = miFormulario.cleaned_data
#             usuario.email = informacion ["email"]
#             usuario.password1 = informacion ["password1"]
#             usuario.password2 = informacion["password2"]
#             usuario.save()
#             return render(request, "inicio.html")
#     else:
#         miFormulario = User_registration_form(initial={"email": usuario.email})
#         return render(request, "editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})

