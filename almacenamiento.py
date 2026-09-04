import json

def cargar_horario():
    try:
        with open("horario.json", "r") as archivo:
            return json.load(archivo)
        # El FileNotFoundError es el error que Python lanza cuando intentas abrir
        # un archivo que no existe todavia; aqui lo atrapamos para que el programa
        # no se rompa, retornando None en vez de detenerse.
    except FileNotFoundError:
        return None
 
 
def guardar_horario_completo(horario):
    with open("horario.json", "w") as archivo:
        # indent es solo una sangria y el json.dump convierte la lista en formato json
        json.dump(horario, archivo, indent=4)