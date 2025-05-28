import json
import os

def cargar_datos_json(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def guardar_datos_json(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)

