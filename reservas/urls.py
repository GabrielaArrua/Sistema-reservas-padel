from django.urls import path
from .views import inicio, lista_reservas, crear_reserva, editar_reserva, eliminar_reserva, registro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reservas/', lista_reservas, name='lista_reservas'),
    path('reservar/', crear_reserva, name='crear_reserva'),
    path('editar/<int:id>/', editar_reserva, name='editar_reserva'),
    path('eliminar/<int:id>/', eliminar_reserva, name='eliminar_reserva'),
    path('registro/', registro, name='registro')

]