def tabla_multiplicar():
    # Solicitar al usuario el número
    numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
    
    # Mostrar la tabla de multiplicar
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Llamar a la función
tabla_multiplicar()
