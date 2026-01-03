from datetime import datetime

FORMATOS_DATA = (
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%d-%m-%Y",
    "%Y/%m/%d"
)

def normalizar_data(data_str):
    if not data_str:
        return None

    data_str = data_str.strip()

    for formato in FORMATOS_DATA:
        try:
            return datetime.strptime(data_str, formato).date()
        except ValueError:
            continue

    return None

