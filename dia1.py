# Variables y tipos de datos

nombre = "ANDRES"
edad = 28
goles = 5
promedio_goles = goles / edad

# Condicionales

if goles > 10:
    print("Gran goleador")
else:
    print("Aún puedes mejorar")

# Bucles

jugadores = ["Juan", "Pedro", "Luis"]
for jugador in jugadores:
    print(jugador)

# Funciones 

def calcular_promedio(lista_goles):
    return sum(lista_goles) / len(lista_goles)

goles_por_partido = [1, 2, 0, 3]
print(calcular_promedio(goles_por_partido))

""" Paso 3: Proyecto práctico — Estadísticas de jugadores
Crea un script que:
• 	Reciba una lista de jugadores y sus goles.
• 	Calcule el promedio de goles por jugador.
• 	Identifique al máximo goleador.
• 	Imprima un resumen. """

jugadores = {
    "Juan": 4,
    "Pedro": 7,
    "Luis": 2,
    "Carlos": 5
}

total_goles = sum(jugadores.values())
promedio = total_goles / len(jugadores)
max_goleador = max(jugadores, key=jugadores.get)

print(f"Promedio de goles: {promedio}")
print(f"Máximo goleador: {max_goleador} con {jugadores[max_goleador]} goles")