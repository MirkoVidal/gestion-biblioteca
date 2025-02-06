import json

def cargar_datos(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(file, datos):
    with open(file, 'w') as f:
        json.dump(datos, f, indent=4)
