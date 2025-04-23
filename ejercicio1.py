def solo_letras(cadena):
    return cadena.isalpha()


while True:
    nombre = input("Ingrese su nombre por favor: ")
    if solo_letras(nombre):
        print("Bienvenido",nombre)
        break
    else:
        print("Error: solo se permiten letras")
