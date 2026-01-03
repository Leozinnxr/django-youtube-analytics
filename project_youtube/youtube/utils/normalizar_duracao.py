from datetime import time


def normalizar_duracao(value):

    try:
        h, m, s = map(int, value.split(":"))
        value = time(h, m, s)
    except ValueError:
        return None
    return value