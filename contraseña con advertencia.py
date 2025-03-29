
Import getpass

def validar_contraseña():
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    confirmar_contraseña = getpass.getpass("Confirme su contraseña: ")

    if contraseña != confirmar_contraseña:
        print("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
        validar_contraseña()
    elif len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Por favor, inténtelo de nuevo.")
        validar_contraseña()
    elif not any(char.isdigit() for char in contraseña):
        print("La contraseña debe contener al menos un número. Por favor, inténtelo de nuevo.")
        validar_contraseña()
    elif not any(char.isupper() for char in contraseña):
        print("La contraseña debe contener al menos una letra mayúscula. Por favor, inténtelo de nuevo.")
        validar_contraseña()
    elif not any(char.islower() for char in contraseña):
        print("La contraseña debe contener al menos una letra minúscula. Por favor, inténtelo de nuevo.")
        validar_contraseña()
    else:
        print("Contraseña válida")

validar_contraseña()
