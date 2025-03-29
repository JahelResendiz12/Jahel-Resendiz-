import random

def juego_piedra_papel_tijeras():
    opciones = ['piedra', 'papel', 'tijeras']
    
    print("Bienvenido al juego Piedra, Papel o Tijeras!")
    while True:
        # Obtener la jugada del usuario
        jugada_usuario = input("Elige tu jugada (piedra, papel, tijeras). Escribe 'salir' para terminar el juego: ").lower()

        # Salir del juego si el usuario lo desea
        if jugada_usuario == 'salir':
            print("Gracias por jugar. ¡Hasta luego!")
            break

        # Verificar que la jugada del usuario sea válida
        if jugada_usuario not in opciones:
            print("Jugada no válida. Por favor, elige entre piedra, papel o tijeras.")
            continue

        # Computadora hace su jugada
        jugada_computadora = random.choice(opciones)
        print(f"La computadora eligió: {jugada_computadora}")

        # Determinar el ganador
        if jugada_usuario == jugada_computadora:
            print("¡Es un empate!")
        elif (jugada_usuario == 'piedra' and jugada_computadora == 'tijeras') or \
             (jugada_usuario == 'papel' and jugada_computadora == 'piedra') or \
             (jugada_usuario == 'tijeras' and jugada_computadora == 'papel'):
            print("¡Ganaste! Felicitaciones.")
        else:
            print("¡Perdiste! La computadora ganó.")

# Iniciar el juego
juego_piedra_papel_tijeras()


