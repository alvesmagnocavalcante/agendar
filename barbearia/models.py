from django.db import models

class Agendamento(models.Model):
    hora = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.hora} Disponível: {self.disponivel}'