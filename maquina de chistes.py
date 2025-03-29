import random

def contar_chisme():
    # Lista de chismes o chistes divertidos
    chismes = [
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",
        "¿Sabías que el perro de Juan está tomando clases de yoga? ¡Es un perro flexible!",
        "Escuché que Carlos va a abrir un restaurante de comida rápida... ¡se llamará 'Comida para llevar'!",
        "¿Por qué el reloj fue al gimnasio? ¡Porque quería ponerse en forma!",
        "¡Parece que Ana va a hacer una fiesta sorpresa, pero nadie sabe a quién va a sorprender!",
        "¿Por qué la computadora fue al médico? Porque tenía un virus.",
        "¿Sabías que Luis va a cambiar su coche por una bicicleta? ¡Quiere pedalear hacia el futuro!",
        "Parece que Marta está organizando una fiesta para su pez. ¡Nunca imaginamos que los peces también tienen fiesta!"
    ]
    
    # Espera a que el usuario presione Enter para contar un chisme
    input("Presiona Enter para escuchar un chisme...")

    # Elegir un chisme aleatorio de la lista
    chisme_aleatorio = random.choice(chismes)

    # Contar el chisme
    print(f"\n¡Chisme aleatorio! {chisme_aleatorio}")

# Ejecutar la función
contar_chisme()
