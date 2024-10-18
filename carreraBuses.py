import os
import random
import time

# Colores
GREN = "\033[32m"
END = "\033[0m"

# Pedir nombres de los jugadores
jugador1 = input("Introduce el nombre del jugador 1: ")
jugador2 = input("Introduce el nombre del jugador 2: ")

# Función para imprimir los buses en la carrera
def buses(n1, n2):
    output = []
    output.append(115 * "-")
    
    # Longitud total disponible para el nombre del jugador (en el bus)
    ancho_bus = 19
    
    # Calcular los espacios para centrar el nombre del jugador 1
    espacios_disponibles1 = ancho_bus - len(jugador1) - 2  # 2 son para los "|)"
    espacios_izquierda1 = espacios_disponibles1 // 2
    espacios_derecha1 = espacios_disponibles1 - espacios_izquierda1
    
    # Crear las líneas del bus del jugador 1
    output.append((n1 * " ") + "_______________  " + ((100 - n1) * " ") + "|")
    output.append((n1 * " ") + "|__|__|__|__|__|___ " + ((97 - n1) * " ") + "|")
    # Centrar el nombre del jugador 1
    output.append((n1 * " ") + "|" + " " * espacios_izquierda1 + jugador1 + " " * espacios_derecha1 + "|)" + ((96 - n1) * " ") + "|")
    output.append((n1 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95 - n1) * " ") + "|")
    output.append(115 * "_")
    
    # Calcular los espacios para centrar el nombre del jugador 2
    espacios_disponibles2 = ancho_bus - len(jugador2) - 2  # 2 son para los "|)"
    espacios_izquierda2 = espacios_disponibles2 // 2
    espacios_derecha2 = espacios_disponibles2 - espacios_izquierda2
    
    # Crear las líneas del bus del jugador 2
    output.append((n2 * " ") + "_______________  " + ((100 - n2) * " ") + "|")
    output.append((n2 * " ") + "|__|__|__|__|__|___ " + ((97 - n2) * " ") + "|")
    # Centrar el nombre del jugador 2
    output.append((n2 * " ") + "|" + " " * espacios_izquierda2 + jugador2 + " " * espacios_derecha2 + "|)" + ((96 - n2) * " ") + "|")
    output.append((n2 * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95 - n2) * " ") + "|")
    output.append(115 * "_")
    return "\n".join(output)


# Variables iniciales
a = 0  # Posición del bus de jugador 1
b = 0  # Posición del bus de jugador 2
gano = None  # Inicializa 'gano' aquí

# Limpiar la pantalla y mostrar la presentación
os.system("cls" if os.name == "nt" else "clear")
presentacion = f"""
        <<<<<<<<<<< CARRERA DE BUSES >>>>>>>>>> 
        {jugador1} VS {jugador2}"""
print(presentacion)
time.sleep(3)

# Bucle de la carrera
while a < 97 and b < 97:
    c = random.randint(1, 2)
    if c == 1:
        a += 1  # Avanza el bus del jugador 1
    else:
        b += 1  # Avanza el bus del jugador 2
    
    # Limpiar pantalla y mostrar la carrera
    os.system("cls" if os.name == "nt" else "clear")
    print(buses(a, b))
    time.sleep(0.07)

# Determinar el ganador
if a >= 97:
    gano = jugador1  # Ganador es el jugador 1
if b >= 97:
    gano = jugador2  # Ganador es el jugador 2

# Imprimir el resultado final
print(f"{GREN}¡GANÓ LA CARRERA: {gano}!{END}")
