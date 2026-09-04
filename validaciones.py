def convertir_a_minutos(hora):
    #El split corta la cadena de texto en cada lugar donde encuentra el carácter ":". Lo use para separa horas y min
    partes = hora.split(":")

    horas_texto = partes[0]
    minutos_texto = partes[1]

    horas = int(horas_texto)
    minutos = int(minutos_texto)

    return horas * 60 + minutos

def hay_choque(evento_existente, nuevo_evento):
# En esta parte solo aploque la logica de A_inicio < B_fin Y B_inicio < A_fin
    # Solo puede haber choque si es el mismo día
    if evento_existente["dia"].strip().title() != nuevo_evento["dia"].strip().title():
        return False

    inicio_existente = convertir_a_minutos(evento_existente["hora_inicio"])
    fin_existente = convertir_a_minutos(evento_existente["hora_fin"])
    inicio_nuevo = convertir_a_minutos(nuevo_evento["hora_inicio"])
    fin_nuevo = convertir_a_minutos(nuevo_evento["hora_fin"])

    # En esta parte aplique la fórmula de arriba
    if inicio_existente < fin_nuevo and inicio_nuevo < fin_existente:
        return True
    else:
        return False