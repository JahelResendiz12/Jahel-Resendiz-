def calcular_total_con_propina():
    # Solicitar el total de la cuenta
    total_cuenta = float(input("Introduce el total de tu cuenta: $"))
    
    # Solicitar el porcentaje de propina
    print("Elige el porcentaje de propina que deseas dejar:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    
    opcion = int(input("Ingresa el número correspondiente a tu opción: "))
    
    # Calcular el monto de la propina
    if opcion == 1:
        porcentaje_propina = 10
    elif opcion == 2:
        porcentaje_propina = 15
    elif opcion == 3:
        porcentaje_propina = 20
    else:
        print("Opción no válida, usando 10% como valor predeterminado.")
        porcentaje_propina = 10
    
    # Calcular el monto de la propina
    propina = total_cuenta * (porcentaje_propina / 100)
    
    # Calcular el total a pagar
    total_a_pagar = total_cuenta + propina
    
    # Mostrar los resultados
    print(f"\nTotal de la cuenta: ${total_cuenta:.2f}")
    print(f"Porcentaje de propina: {porcentaje_propina}%")
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar (cuenta + propina): ${total_a_pagar:.2f}")

# Iniciar el cálculo
calcular_total_con_propina()
