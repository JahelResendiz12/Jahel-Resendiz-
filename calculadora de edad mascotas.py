def convertir_edad():
    # Solicitar al usuario el tipo de animal
    animal = input("¿De qué animal quieres saber la edad en años humanos? (perro/gato): ").lower()

    # Verificar si el animal es perro o gato
    if animal == "perro":
        # Solicitar la edad del perro
        edad_perro = int(input("Introduce la edad del perro en años: "))
        # Calcular la edad equivalente en años humanos
        edad_humana = edad_perro * 7
        print(f"La edad del perro de {edad_perro} años equivale a {edad_humana} años humanos.")
    
    elif animal == "gato":
        # Solicitar la edad del gato
        edad_gato = int(input("Introduce la edad del gato en años: "))
        # Calcular la edad equivalente en años humanos
        edad_humana = edad_gato * 5
        print(f"La edad del gato de {edad_gato} años equivale a {edad_humana} años humanos.")
    
    else:
        print("Lo siento, solo puedo convertir la edad de perros o gatos.")

# Llamar a la función para ejecutar el programa
convertir_edad()
