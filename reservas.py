import json
from datos import funciones, salas, peliculas

RUTA_JSON = "reservas_cargadas.json"

def cargar_reservas_json():
    """Lee las reservas desde el archivo JSON."""
    try:
        with open(RUTA_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe todavía o está vacío, 
        # devolvemos una lista vacía para que el programa no falle.
        return []

def guardar_reserva_json(nuevas_reservas):
    """Guarda la lista actualizada de reservas en el archivo JSON."""
    with open(RUTA_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(nuevas_reservas, archivo, indent=4, ensure_ascii=False)
