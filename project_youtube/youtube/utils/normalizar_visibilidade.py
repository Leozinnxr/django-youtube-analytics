

def normalizar_visibilidade(visibilidade):
    if not visibilidade:
        return None

    return visibilidade.upper().replace("Ú", "U").strip()