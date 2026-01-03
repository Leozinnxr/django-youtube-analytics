from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator

from youtube.models import BaseModel
from django.db import models


class Canal(BaseModel):

    canal_id = models.CharField(max_length=12, unique=True, verbose_name="ID do canal",
                                validators=[RegexValidator(regex=r'^UC\d+$',), MinLengthValidator(12)])

    canal_nome = models.CharField(max_length=100, verbose_name="Nome do canal", unique=True,
                                  validators=[MinLengthValidator(3)])

    canal_inscritos = models.IntegerField(default=0, verbose_name="Inscritos", validators=[MinValueValidator(0)])


    def clean(self):
        try:
            if not self.canal_nome.strartswitch("Canal"):

                raise ValidationError("")

        except ValidationError as e:
            print(e)