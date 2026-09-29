canciones = ["Contigo quiero amores", "Hollywood", "Smack that", "Llamala", "No se si fue"]

#Como se accede a los elementos de la lista
num = len(canciones)
print(num)

#Recorrer una lista

# for cancion in canciones:
#     print(cancion)
# for var in range(len(canciones)):
#     print(canciones[var])

# Imprimir las canciones en orden inverso
for var in range(4, -1, -1):
    print(canciones[var])