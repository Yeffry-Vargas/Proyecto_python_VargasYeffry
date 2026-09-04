from almacenamiento import cargar_horario, guardar_horario_completo
from validaciones import hay_choque
import json

horario = [
    
    {
        "materia": "Matematicas",
        "dia": "Lunes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "ubicacion": "Aula 101"
    },
    {
        "materia": "Programacion",
        "dia": "Martes ",
        "hora_inicio": "11:00",
        "hora_fin": "13:00",
        "ubicacion": "Laboratorio 3"
    },
    {
        "materia": "Ingles",
        "dia": "Miercoles",
        "hora_inicio": "14:00",
        "hora_fin": "15:00",
        "ubicacion": "Aula 208"
    },
    {
        "materia": "Psicologia",
        "dia": "Jueves",
        "hora_inicio": "16:00",
        "hora_fin": "17:00",
        "ubicacion": "Laboratorio 2"
    },
    {
        "materia": "Fisica",
        "dia": "viernes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "ubicacion": "Aula 101"
    }
]


horario_guardado = cargar_horario()

if horario_guardado is not None:
    horario = horario_guardado


opcion = ""
while opcion != "6":




    print("==========================================")
    print("GENERADOR DE HORARIOS PARA ESTUDIANTES")
    print("==========================================")
    print("1. Registrar una materia o actividad")
    print("2. Ver horarios")
    print("3. Modificar una materia o actividad")
    print("4. Eliminar una materia o actividad")
    print("5. Generar reporte del horario")
    print("6. Salir")
    print("==========================================")
    opcion = input("Seleccione una opcion: ")


    if opcion == "1":
        print("Elegiste registrar")

        materia = input("Ingrese el nombre de la matria/actividad: ")
        dia = input("Ingrese el dia: ")
        hora_inicio = input("Ingrese la hora de inicio (Escribir en formato 24H): ")
        hora_fin = input("Ingrese la hora de finalizacion (Escribir en formato 24H): ")
        ubicacion = input("Ingrese la ubicacion: ")
        nuevo_evento = {
            "materia": materia,
            "dia": dia,
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin,
            "ubicacion": ubicacion
        }

        choque_encontrado = False
        for evento in horario:
            if hay_choque(evento, nuevo_evento):
                choque_encontrado = True
        if choque_encontrado == True:
            print("No se puede registrar, hay un choque de horario con otra materia.")
        else:
            horario.append(nuevo_evento)
            guardar_horario_completo(horario)
            print(f'La materia/actividad {materia} quedo registrada para el {dia} a las {hora_inicio} hasta las {hora_fin} en {ubicacion}. ')

    elif opcion == "2":
        for evento in horario:
            print(f"{evento['dia']}: {evento['materia']} ({evento['hora_inicio']} - {evento['hora_fin']}) en {evento['ubicacion']}")

    elif opcion == "3":
        print("¿Que materia/actividad deseas modificar?")

        materia_buscar = input("Ingrese el nombre de la materia/actividad a modificar: ")
        dia_buscar = input("Ingrese el dia de esa materia/actividad: ")

        encontrado = False

        #Enumerate me recorre un objeto iterable como la lista y obtiene la posicion y el valor de cada elemento
        for indice, evento in enumerate(horario):

            if evento["materia"] == materia_buscar and evento["dia"] == dia_buscar:
                encontrado = True
                nueva_materia = input("Ingrese la nueva materia/actividad: ")
                nuevo_dia = input("Ingrese el dia nuevo: ")
                nuevo_hora_inicio = input("Ingrese la nueva hora en que incia: ")
                nuevo_hora_fin = input("Ingrese la nueva hora en que termina: ")
                nueva_ubicacion = input("Ingrese la nueva ubicacion: ")

                if nueva_materia != "":
                    materia_final = nueva_materia
                else:
                    materia_final = evento["materia"]

                if nuevo_dia != "":
                    dia_final = nuevo_dia
                else:
                    dia_final = evento["dia"]

                if nuevo_hora_inicio !="":
                    hora_inicio_final = nuevo_hora_inicio
                else:
                    hora_inicio_final = evento["hora_inicio"]

                if nuevo_hora_fin!="":
                    hora_fin_final = nuevo_hora_fin
                else:
                    hora_fin_final = evento ["hora_fin"]

                if nueva_ubicacion !="":
                    ubicacion_final = nueva_ubicacion
                else:
                    ubicacion_final = evento ["ubicacion"]

                evento_probado = {
                     "materia": materia_final,
                    "dia": dia_final,
                    "hora_inicio": hora_inicio_final,
                    "hora_fin": hora_fin_final,
                    "ubicacion": ubicacion_final
                }
                #aqui valide la alidacion de choque excluyendo el propio evento que se esta editando
                choque_encontrado = False
                for otro_evento in horario:
                    if otro_evento is not evento:
                        if hay_choque(otro_evento, evento_probado):
                            choque_encontrado = True

        if encontrado == False:
            print("Materia/actividad no encontrada para ese dia. ") 

        elif choque_encontrado == True:
            print("No se puede modificar hay un choque de horario con otra materia.")

        else:
            horario[indice] = evento_probado
            guardar_horario_completo(horario)
            print("Materia/actividad modificada exitosamente. ")
        
    elif opcion == "4":
        print("¿Que materia/actividad deseas eliminar?")

        materia_eliminar = input("Ingrese el nombre de la materia/actividad a eliminar: ")
        dia_eliminar = input("Ingrese el dia: ")

        encontrado = False

        for evento in horario:
            if evento ["materia"] == materia_eliminar and evento ["dia"] == dia_eliminar:
                horario.remove(evento)
                encontrado = True
                guardar_horario_completo(horario)

                # rompe el ciclo apenas elimino, ya no necesito seguir buscando
                break
        if encontrado == False:
            print("La materia/actividad no se encontro. ")
        else:
            print("Materia/actividad eliminada exitosamente. ")

    elif opcion == "5":
        print("Generar reporte del horario")

        dia_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        reporte = []

        for dia in dia_semana:
            print(f"{dia}: ")
            eventos_del_dia = []

            for evento in horario:
                if evento["dia"].strip().title() == dia:
                    print(f"- {evento['materia']} ({evento['hora_inicio']} - {evento['hora_fin']}) en {evento['ubicacion']}")
                    eventos_del_dia.append(evento)

            dia_reporte = {"dia": dia, "eventos": eventos_del_dia}
            reporte.append(dia_reporte)

            input('Presione "ENTER" para continuar...')
        with open ("reporte_horario.json", "w",) as archivo:
            #el json.dump conviente un archivo en formato json
            #indent es solo una sangria
            json.dump(reporte, archivo, indent=4)

        
    elif opcion == "6":
        print("Saliendo del programa...")
    elif opcion > "6":
        print("Solo hay 6 opciones, intenta de nuevo")
    else:
        print("Error, no puedes escribir letras. Intenta nuevamente")
