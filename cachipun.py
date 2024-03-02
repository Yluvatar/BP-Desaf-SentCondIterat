
import random
import sys

try:

    jugador = sys.argv[1]

    if jugador.lower() != "piedra" and jugador.lower() != "papel" and jugador.lower() != "tijera":

        print("\nDebe jugar Piedra, Papel o Tijera")

    else:

        opciones = ["Piedra", "Papel", "Tijera"]

        opcion_random = random.choice(opciones)

        if opcion_random.lower() == jugador.lower():
            ganador = "Empate"
        elif opcion_random.lower() == "piedra" and jugador.lower() == "tijera":
            ganador = "Perdiste"
        elif opcion_random.lower() == "papel" and jugador.lower() == "piedra":
            ganador = "Perdiste"
        elif opcion_random.lower() == "tijera" and jugador.lower() == "papel":
            ganador = "Perdiste"
        else:
            ganador = "Ganaste!!!"

        print("\n")

        print(f"Tú jugaste {jugador}")
        print(f"Computador jugó {opcion_random}")
        print(f"{ganador}")

except IndexError:

    print("\nSe produjo un error de argumentos necesarios")

finally:

    print("\n Fin del Juego!!")

print("\n")
