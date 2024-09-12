# Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor, ingrese la edad del cliente: "))


# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca
permitido = True if edad >= 18 else False 
    
# Paso 3: Mostrar al usuario si su cliente puede ingresar o no a la discoteca

if permitido:
    print("Puedes ingresar a la discoteca")
else:
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad")