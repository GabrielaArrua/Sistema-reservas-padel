from django.db import models
from django.contrib.auth.models import User

class Cancha(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
HORARIOS = [
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
]
    
class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario = models.CharField(max_length=5, choices=HORARIOS)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_cliente} - {self.cancha}'


