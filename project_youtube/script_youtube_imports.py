from decimal import Decimal
from django.core.exceptions import ValidationError
from manage import *
import contextlib, io
from youtube.utils import normalizar_qualidade, normalizar_visibilidade, normalizar_duracao, normalizar_duracao, \
    normalizar_data, normalizar_idioma
from youtube.utils.normalizar_url import normalizar_url

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from youtube.models import Video, Canal, Categoria, Playlist
from youtube.enumerations import Visibilidade, QualidadePx

Video = set(Video.objects.all())
Canal = set(Canal.objects.all())
Categoria = set(Categoria.objects.all())
Playlist = set(Playlist.objects.all())
total = 0
erros = 0


with open('pessoas.csv', 'r', encoding='UTF-8') as arquivo:
    try:
        arquivo.readline()
        for linha in arquivo:
            dados = linha.split(',')
            video_id = dados[0]
            url = dados[1]
            titulo = dados[2]
            likes = int(dados[3])
            dislikes = int(dados[4])
            salvos = int(dados[5])
            downloads = int(dados[6])
            duracao = dados[7]
            comentarios = int(dados[8])
            qualidade_px = dados[9]
            canal_id = dados[10].strip()
            canal_nome = dados[11].strip()
            canal_inscritos = int(dados[12])
            categorias = dados[13].split(";")
            palavras_chaves = dados[14]
            descricao = dados[15]
            data_postagem = dados[16]
            visibilidade = dados[17]
            playlist_id = dados[18]
            playlist_nome = dados[19]
            idioma = dados[20]


            if qualidade_px == '360' or qualidade_px == '0':
                qualidade_px = qualidade_px.P360
            elif qualidade_px == '480':
                qualidade_px = qualidade_px.P480
            elif qualidade_px == '720':
                qualidade_px = qualidade_px.P720
            elif qualidade_px == '1080':
                qualidade_px = qualidade_px.P1080
            elif qualidade_px == '1440':
                qualidade_px = qualidade_px.P1440
            elif qualidade_px == '2160':
                qualidade_px = qualidade_px.P2160
            else:
                qualidadde_px = normalizar_qualidade(qualidade_px)


            if visibilidade.upper() == 'PUBLICO':
                visibilidade = Visibilidade.PUBLICO
            elif visibilidade.upper() == 'PRIVADO':
                visibilidade = Visibilidade.PRIVADO
            else:
                visibilidade= normalizar_visibilidade(visibilidade)



            if "www.youtube.com" in url and not "https://" in url:
                url = "https://" + url
                url.full_clean()
                url.save()
            else:
                url = normalizar_url(url)

            try:
                duracao = normalizar_duracao(duracao)
                duracao.full_clean()
                duracao.save()
            except ValidationError as e:
                print(e)

            for categoria in categorias:
                categorias = categoria

            for palavra in palavras_chaves:
                palavras_chaves = palavra

            try:
                data_postagem = normalizar_data(data_postagem)
                idiomas = normalizar_idioma(idioma)
            except ValidationError as e:
                print(e)


    except Exception as e:
        print(f"Problema: {e} com registro {linha}")
        erros += 1

    print(f"Processamento concluído com {total} processados e {erros} erros")


