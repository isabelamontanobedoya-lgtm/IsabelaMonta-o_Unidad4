def cargar_cajas(pesos, peso_maximo):

cajas_cargadas = []
peso_total = 0

for i in range(len(cajas_cargadas))
     peso_total += i 
    
    if peso_total > peso_maximo: 
        peso_total -= i
        cajas_cargadas.append(i)
        
#Datos de prueba
peso_cakas = [120, 400, 300, 180, 450, 200]
peso_max_avion = 100

cargar_cajas(pesos_cajas, pesos_max_avion)
