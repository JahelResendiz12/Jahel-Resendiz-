def contar_letras():
    # Solicitar al usuario una palabra
    palabra = input("Introduce una palabra: ")
    
    # Eliminar los espacios de la palabra
    palabra_sin_espacios = palabra.replace(" ", "")
    
    # Contar las letras
    cantidad_letras = len(palabra_sin_espacios)
    
    # Mostrar la cantidad de letras
    print(f"La cantidad de letras en la palabra (sin contar los espacios) es: {cantidad_letras}")

# Llamar a la función
contar_letras()
