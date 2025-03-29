edad = int(input("ingrese su edad: "))
if edad < 18:
     print("eres menor de edad: ")
elif edad >= 18 and edad < 65:
    print("eres adulto")
else: 
    print("eres jubilado")  