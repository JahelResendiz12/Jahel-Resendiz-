def contar_palabras():
    # Pedir al usuario una frase
    frase = input("Introduce una frase: ")

    # Usar split() para dividir la frase en palabras
    palabras = frase.split()

    # Contar las palabras usando un ciclo for
    contador = 0
    for palabra in palabras:
        contador += 1

    # Mostrar el número de palabras
    print(f"La frase tiene {contador} palabras.")

# Llamar a la función
contar_palabras()
