from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from youtube.enumerations import QualidadePx, Visibilidade
from youtube.models import BaseModel


class Video(BaseModel):

    video_id = models.CharField(max_length=11, verbose_name="Video ID", unique=True,
                                validators=[MinLengthValidator(11)])


    url = models.CharField(max_length=43, verbose_name="URL", unique=True,
                           validators=[MinLengthValidator(43)])


    titulo = models.CharField(max_length=100, verbose_name="Titulo", validators=[MinLengthValidator(5)])

    likes = models.IntegerField(verbose_name="Likes", validators=[MinValueValidator(0)])

    deslikes = models.IntegerField(verbose_name="Deslikes", validators=[MinValueValidator(0)])

    salvos = models.IntegerField(verbose_name="Salvos", validators=[MinValueValidator(0)])

    downloads = models.IntegerField(verbose_name="Downloads", validators=[MinValueValidator(0)])

    #TODO fazer o minvalue e maxvalue de duração
    duracao = models.TimeField(verbose_name="Duração", auto_now=False, auto_now_add=False)

    comentarios = models.IntegerField(verbose_name="Comentários", validators=[MinValueValidator(0)])

    qualidade_px = models.CharField(verbose_name="Qualidade", max_length=5,
                                    validators=[MinLengthValidator(3)], choices=QualidadePx)

    descricao = models.TextField(verbose_name="Descrição do vídeo", max_length=400,validators=[MinLengthValidator(3)])


    data_postagem = models.DateField(verbose_name="Data do video",
                                     auto_now=False, auto_now_add=False)

    visibilidade = models.CharField(verbose_name="Visibilidade", max_length=7,
                                    validators=[MinLengthValidator(7)], choices=Visibilidade)


    def clean(self):

        try:
            if not self.url.startswith("https://www.youtube.com/watch?v="):
                raise ValidationError("")
        except ValidationError as e:
            print(e)