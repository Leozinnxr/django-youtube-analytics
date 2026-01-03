from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from youtube.models import BaseModel


class Playlist(BaseModel):

    playlist_id = models.CharField(max_length=9, verbose_name="Playlist ID",
                                   validators=[MinLengthValidator(9)])

    playlist_nome = models.CharField(max_length=100, verbose_name="Nome da Playlist",
                                     validators=[MinLengthValidator(5)])

    def clean(self):

        try:
            if not self.playlist_id.startswith("PL"):
                raise ValidationError("")
        except ValidationError as e:
            print(e)