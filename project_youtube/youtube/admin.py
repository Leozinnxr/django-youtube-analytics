from django.contrib import admin
from youtube.models import *


# Register your models here.
admin.site.register((Canal, Categoria, Playlist, Video))