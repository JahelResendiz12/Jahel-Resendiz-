def robot_responde():
    print("Hola, soy un robot. ¿En qué puedo ayudarte?")
    
    while True:
        usuario_input = input("Tú: ").lower()  # Se lee la entrada del usuario y se convierte a minúsculas
        
        if 'hola' in usuario_input:
            print("Robot: ¡Hola! ¿Cómo estás?")
        elif 'adiós' in usuario_input:
            print("Robot: ¡Adiós! ¡Cuídate!")
            break
        elif 'cómo estás' in usuario_input:
            print("Robot: Estoy bien, gracias por preguntar. ¿Y tú?")
        elif 'nombre' in usuario_input:
            print("Robot: Soy un robot sin nombre. ¿Cómo te llamas tú?")
        elif 'gracias' in usuario_input:
            print("Robot: ¡De nada!")
        else:
            print("Robot: No entendí eso. ¿Puedes repetirlo?")

# Iniciar el robot
robot_responde()
