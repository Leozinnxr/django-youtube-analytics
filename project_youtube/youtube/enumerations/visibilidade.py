from django.db import models


class Visibilidade(models.TextChoices):

    PUBLICO = 'PUBLICO', 'PUBLICO'
    PRIVADO = 'PRIVADO', 'PRIVADO'
