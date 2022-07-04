from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from users.models import User_profile

# Create your views here.

class editarperfil(LoginRequiredMixin, UpdateView):
    model =  User_profile
    template_name = "editar_perfil.html"
    fields = ["user", "image"]
    print(model)

    def get_success_url(self):
        return reverse("inicio", kwargs={"pk":self.object.pk})