def verificar_numero():
    # Solicitar al usuario un número
    numero = float(input("Introduce un número: "))
    
    # Verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# Llamar a la función
verificar_numero()
