from django.db.models import QuerySet
from .base_manager import BaseManager
from ..models import Video


class VideoManager(BaseManager):

    def publicos(self) -> QuerySet['Video']:
        return Video.objects.filter(visibilidade = "PUBLICO")

    def privados(self) -> QuerySet['Video']:
        return Video.objects.filter(visibilidade = "PRIVADO")

    def videos_do_canal(self, canal_youtube_id: str) -> QuerySet['Video']:
        canal = Video.objects.filter(canal_youtube_id = canal_youtube_id)




