#EJERCICIO 1
# Creamos un objeto (en este caso, un numero)
altitud = 10000 # metros

# 'altitud' es na etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud 

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud) # 10000
print(elevacion) # 9500

# altitud = "muy alto"
# print(altitud)

#EJERCICIO 2
velocidad = 800 # km/h
print(id(velocidad)) # Muestra el identificador unico

otra_velocidad = 800
print(id(otra_velocidad)) # Para numeros pequeños, Python

lista1 = [1, 3, 67]
print(id(lista1))

#EJERCICIO 3
modelo = "Boeing 747"
print(id(modelo)) # Guardamos el ID oroginal

# Intentamos "modificar" el string
modelo = modelo + "-800"
print(modelo) # "Boeing 747-800"
print(id(modelo)) # ¡ID diferente! se creo un nuevo objeto


