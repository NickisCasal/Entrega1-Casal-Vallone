from django.urls import path
from primermvt.views import crear_familiar, crear_mascota, crear_vehiculo, show_familiar, show_mascota, show_vehiculo, search_view, detail_familiar, eliminar_familiar, detail_mascota, eliminar_mascota, detail_vehiculo, eliminar_vehiculo, editar_familiar, editar_mascota,editar_vehiculo


urlpatterns = [
    path("grupofliar/", crear_familiar.as_view(), name = "grupofliar"),
    path("mascota/", crear_mascota.as_view(), name = "mascota"),
    path("vehiculo/", crear_vehiculo.as_view(), name = "vehiculo"),
    path("familiares/", show_familiar, name = "list_familiares"),
    path("mascotas/", show_mascota, name = "mascotas"),
    path("vehiculos/", show_vehiculo, name = "vehiculos"),
    path("search/", search_view, name = "search"),
    path("familiar_detalle/<int:pk>/", detail_familiar, name = "detail_familiar"),
    path("eliminar_familiar/<int:pk>/", eliminar_familiar, name = "eliminar_familiar"),
    path("mascota_detalle/<int:pk>/", detail_mascota, name = "detail_mascota"),
    path("eliminar_mascota/<int:pk>/", eliminar_mascota, name = "eliminar_mascota"),
    path("vehiculo_detalle/<int:pk>/", detail_vehiculo, name = "detail_vehiculo"),
    path("eliminar_vehiculo/<int:pk>/", eliminar_vehiculo, name = "eliminar_vehiculo"),
    path("editar_familiar/<int:pk>/", editar_familiar.as_view(), name = "editar_familiar"),
    path("editar_mascota/<int:pk>/", editar_mascota.as_view(), name = "editar_mascota"),
    path("editar_vehiculo/<int:pk>/", editar_vehiculo.as_view(), name = "editar_vehiculo")
]
