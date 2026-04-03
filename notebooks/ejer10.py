# src/procesamiento.py

def calcular_posiciones_por_ronda(rounds):
    posiciones = {}
    for r in rounds:
        tema = r["theme"]
        aux = {}
        for nombres, jueces in r["scores"].items():
            total = jueces["judge_1"] + jueces["judge_2"] + jueces["judge_3"]
            aux[nombres] = total
        
        posiciones[tema] = sorted(aux.items(), key=lambda x: x[1], reverse=True)
    return posiciones

def generar_tabla_final(posiciones):
    tabla_final = {}
    for tema in posiciones:
        participantes = posiciones[tema]
        for i in range(len(participantes)):
            nombre = participantes[i][0]
            puntaje = participantes[i][1]
            
            if nombre not in tabla_final:
                tabla_final[nombre] = {
                    "puntaje": 0, "rondas ganadas": 0, 
                    "mejor ronda": 0, "promedio": 0
                }
            
            tabla_final[nombre]["puntaje"] += puntaje
            if puntaje > tabla_final[nombre]["mejor ronda"]:
                tabla_final[nombre]["mejor ronda"] = puntaje
            if i == 0: 
                tabla_final[nombre]["rondas ganadas"] += 1
                
    for nombre in tabla_final:
        tabla_final[nombre]["promedio"] = tabla_final[nombre]["puntaje"] / len(posiciones)
        
    return sorted(tabla_final.items(), key=lambda x: x[1]["puntaje"], reverse=True)