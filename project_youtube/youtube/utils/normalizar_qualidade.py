

def normalizar_qualidade(valor):

    if not valor:
        return None

    return (valor.upper().replace("PX", "").replace("P", "").replace(".", "").strip())
