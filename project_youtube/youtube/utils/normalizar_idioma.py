def normalizar_idioma(value):
    if not value:
        return None

    idiomas_validos = ("pt-BR", "pt-PT", "en", "en-US", "es", "es-ES")

    value = value.strip()

    value = value.lower()

    if value == "portugues" or value == "português":
        return "pt-BR"

    if "-" in value:
        partes = value.split("-")
        if len(partes) == 2:
            value = partes[0].lower() + "-" + partes[1].upper()
    else:
        if len(value) == 4:
            value = value[:2].lower() + "-" + value[2:].upper()
        elif len(value) == 2:
            value = value.lower()

    if value in idiomas_validos:
        return value

    return None
