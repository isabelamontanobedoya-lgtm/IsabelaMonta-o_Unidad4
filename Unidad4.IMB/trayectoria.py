
def analizar_trayectoria(rumbo_planeado:list, rumbo_real:list, umbral_desviacion=5):
    #Crear una lista vacía para los índices
    indices = []
    #hay que verificar que las listas sean de igual lomgitud
    if not rumbo_planeado or not rumbo_real:
        return None

    if len(rumbo_planeado) != len(rumbo_real):
        return None
    #Recorrer cada elemento, calculamos la diferencia y
    #comprobamos si es mayor que 5. Si es así, ponemos el índice
    #dentro de la lista vacía
    for i in range(len(rumbo_planeado)):
        dif = abs(rumbo_planeado[i] - rumbo_real[i]) 
        if dif > umbral_desviacion:
            indices.append(i)

    return indices


# Datos de prueba
planeado = [45, 45, 45, 90, 90, 90, 170, 180, 225, 225, 270]
real =     [43, 47, 48, 86, 91, 95, 183, 176, 222, 230, 265]

# Probando la función
#desviaciones = analizar_trayectoria(planeado, real, 5)
a = 0
b = 10
desviaciones = analizar_trayectoria(a, b, 5)


if not desviaciones:
    print("No hay desviaciones significativas")
elif desviaciones != None:
    print(f"Se detectaron desviaciones significativas en los puntos: {desviaciones}")
else:
    print("Revise los datos enviados")

