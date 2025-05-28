import pandas as pd
import os
import json

def cargar_datos_json(archivo):
    if not os.path.exists(archivo):
        return pd.DataFrame()
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return pd.DataFrame(datos)
    except json.JSONDecodeError:
        return pd.DataFrame()

def guardar_datos_json(df, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, indent=4, ensure_ascii=False)

