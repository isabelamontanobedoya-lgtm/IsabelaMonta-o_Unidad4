#Diccionario vacio
aeronave = {}

#Dicciorio con elementos
aeronave = { 
    "modelo": "Boeing 787-9",
    "envergadura": 60.17, # metros
    "longitud": 62.81,    # metros
    "mtow": 254000,       # kg
    "velocidad_max": 954  # km/h
}

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

# Creación con dict()
motor = dict(fabricantes="GE", modelo="GE9X", empuje=470, nypass_ratio=10)


#Accedemos a los datos 

print("El modelo del avión es: ", aeronave ["modelo"])
print(f"Su peso máximo de despegue es: {aeronave["mtow"]}")

# Agregar una clave: valor adicional al diccionario
aeronave ["cap_pasajeros"] = 300

print(f"su capacidad de pasajeros es: {aeronave["cap_pasajeros"]}")

aeronave["chequeos"] = [1, 2, 3, 4, 5]

vuelo["destino"] = "MDE"

print("Capitan del vuelo: ", vuelo["tripulacion"][0])

l = aeronave.get("longitud", "Clave no encontrada")
print(l)

# Recorrer un diccionario completo

for clave in vuelo:  #devuelve el valor y clave de los diccionarios anteriores
    print(f"clave: {clave} - valor {vuelo[clave]}")

for clave, valor in vuelo.items():
    print(clave, "-", valor)
