from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from youtube.models import BaseModel


class Categoria(BaseModel):

    categorias = models.CharField(max_length=50, verbose_name="Categoria",
                                  validators=[MinLengthValidator(5)])

    palavras_chave = models.CharField(max_length=130, verbose_name="Palavras chave",
                                      validators=[MinLengthValidator(4)])


    #TODO no script separar as categorias

