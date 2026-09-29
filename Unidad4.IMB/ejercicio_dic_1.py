vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE",
}

ciudad_llegada = vuelo["destino"]
print("ciudad_llegada")

vuelo["destino"] = "CLO"
print(vuelo)

vuelo["estado"] = "en el aire"
print(vuelo)

piloto = vuelo.get("piloto", "piloto no asignado")
print(piloto)