from django.db import models


class QualidadePx(models.TextChoices):

    P360: '360', '360'
    P480: '480', '480'
    P720: '720', '720'
    P1080: '1080', '1080'
    P1440: '1440', '1440'
    P2160: '2160', '2160'
