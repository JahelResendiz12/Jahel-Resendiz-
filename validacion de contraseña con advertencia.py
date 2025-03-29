import re

def validar_contraseña():
    # Solicitar la contraseña al usuario
    contraseña = input("Introduce tu contraseña: ")
    
    # Verificar la longitud de la contraseña
    if len(contraseña) < 8:
        print("¡Advertencia! La contraseña debe tener al menos 8 caracteres.")
        return False
    
    # Verificar si contiene al menos una letra mayúscula
    if not re.search("[A-Z]", contraseña):
        print("¡Advertencia! La contraseña debe contener al menos una letra mayúscula.")
        return False
    
    # Verificar si contiene al menos una letra minúscula
    if not re.search("[a-z]", contraseña):
        print("¡Advertencia! La contraseña debe contener al menos una letra minúscula.")
        return False
    
    # Verificar si contiene al menos un número
    if not re.search("[0-9]", contraseña):
        print("¡Advertencia! La contraseña debe contener al menos un número.")
        return False
    
    # Si pasa todas las validaciones
    print("Contraseña válida.")
    return True

# Llamar a la función de validación
validar_contraseña()
