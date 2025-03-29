def validar_entrada():
    while True:
        try:
            # Solicitar un número entero positivo
            numero = int(input("Introduce un número entero positivo: "))
            
            # Validar que el número sea positivo
            if numero > 0:
                print(f"¡Número válido! Has ingresado: {numero}")
                break  # Salir del ciclo si la entrada es correcta
            else:
                print("¡Advertencia! El número debe ser positivo. Intenta de nuevo.")
        except ValueError:
            print("¡Error! Debes ingresar un número entero. Intenta de nuevo.")

# Llamar a la función para ejecutar la validación
validar_entrada()
