from django.db.models import QuerySet
from .base_manager import BaseManager
from ..models import Video


class VideoManager(BaseManager):

    def publicos(self) -> QuerySet['Video']:
        return Video.objects.filter(visibilidade = "PUBLICO")

    def privados(self) -> QuerySet['Video']:
        return Video.objects.filter(visibilidade = "PRIVADO")




