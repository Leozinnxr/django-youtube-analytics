from django.db import models


class QualidadePx(models.TextChoices):

    P360 = 'P360', '360'
    P480 = 'P480', '480'
    P720 = 'P720', '720'
    P1080 = 'P1080', '1080'
    P1440 = 'P1440', '1440'
    P2160 = 'P2160', '2160'
