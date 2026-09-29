from random import randint, uniform

#lista vacía
lista = []

#método append para agregar elementos 
dato = randint(0,100)
lista.append(dato)
#Guardar 10 datos mas dentro de la lista
for i in range(10):
    i = lista.append(randint(0,100))
print(lista)

#Craer dos listas nuevas: la primera va a contener los pares y la segunda los impares

#listas nuevas
pares = []
impares = []

for i in lista:
    if i %2 == 0:
        pares.append(i)
    else:
        impares.append(i)

#Calcular el promedio de lista, pares e impares

#prom_lista 
suma = 0

for i in lista:
    suma += dato

prom = suma/len(lista)

#prom_pares
suma_pares = 0

for datos in lista:
    suma_pares += dato

prom_pares = suma_pares/len(pares)

#prom_impares
suma_impares = 0

for datos in lista:
    suma_impares += dato

prom_impares = suma_impares/len(impares)

print("promedio de lista", prom_lista)
print("promedio de pares", prom_pares)
print("promedio de impares", prom_impares)


#ejercicios

