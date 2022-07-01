from django.urls import path
from primermvt.views import grupofliar, mascotas, vehiculos, show_familiar, show_mascota, show_vehiculo, search_view, detail_familiar, eliminar_familiar


urlpatterns = [
    path("grupofliar/", grupofliar, name = "grupofliar"),
    path("mascota/", mascotas, name = "mascota"),
    path("vehiculo/", vehiculos, name = "vehiculo"),
    path("familiares/", show_familiar, name = "familiares"),
    path("mascotas/", show_mascota, name = "mascotas"),
    path("vehiculos/", show_vehiculo, name = "vehiculos"),
    path("search/", search_view, name = "search"),
    path("familiar_detalle/<int:pk>/", detail_familiar, name = "detail_familiar"),
    path("eliminar_familiar/<int:pk>/", eliminar_familiar, name = "eliminar_familiar")
]
