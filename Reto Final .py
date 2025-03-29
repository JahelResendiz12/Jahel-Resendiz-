import random

def juego_codigo_secreto():
    # Generar el diccionario con números aleatorios y expresiones matemáticas
    codigo_secreto = {
        3: "5 + 4 - 6",
        7: "3 * 3 - 2",
        2: "10 // 5",
        9: "8 + 1",
        4: "16 // 4"
    }
    
    # Informar al usuario sobre las reglas del juego
    print("Bienvenido al juego 'Descifra el Código Secreto'!")
    print("Debes resolver los problemas matemáticos para desbloquear el código secreto.")
    
    # Inicializar una variable para verificar si el usuario adivina correctamente todas las respuestas
    respuestas_correctas = True
    
    # Recorrer el diccionario y mostrar los problemas
    for clave, expresion in codigo_secreto.items():
        print(f"\nProblema: {expresion} = ?")
        
        # Pedir la respuesta del usuario
        try:
            respuesta_usuario = int(input("Tu respuesta: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            respuestas_correctas = False
            break
        
        # Evaluar la expresión y verificar si la respuesta es correcta
        if respuesta_usuario == eval(expresion):
            print("¡Correcto!")
        else:
            print(f"¡Incorrecto! La respuesta correcta era: {eval(expresion)}")
            respuestas_correctas = False
            break
    
    # Verificar si todas las respuestas fueron correctas
    if respuestas_correctas:
        print("\n¡Código Descifrado! ¡Felicidades, has desbloqueado el código secreto!")
    else:
        print("\nAcceso Denegado. Inténtalo de nuevo.")

# Ejecutar el juego
juego_codigo_secreto()
