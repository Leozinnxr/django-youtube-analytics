import csv
from django.core.management.base import BaseCommand
from youtube.models import Video, Canal
from youtube.utils import normalizar_duracao, normalizar_idioma, normalizar_data

class Script(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('arquivo', type=str)

    def handle(self, *args, **options):
        arquivo = options['arquivo']
        erros = 0
        total = 0

        with open(arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for linha in reader:
                total += 1
                try:
                    canal, _ = Canal.objects.get_or_create(
                        canal_id=linha['canal_id'].strip()
                    )

                    video = Video(
                        titulo=linha['titulo'].strip(),
                        visibilidade=linha['visibilidade'].upper(),
                        data_publicacao=normalizar_data(linha['data']),
                        canal=canal
                    )

                    video.full_clean()
                    video.save()

                except Exception as e:
                    erros += 1
                    self.stderr.write(
                        f"Erro na linha {total}: {e}"
                    )
                    continue

        self.stdout.write(
            self.style.SUCCESS(
                f"Importação finalizada. Total: {total} | Erros: {erros}"
            )
        )
