"""
Ej 53.-generar clave .
Hacer un programa que solicite el ingreso de el nombre, el apellido y el año de nacimiento de una persona.
Generar una clave provisoria de la sig.forma: La primera letra del nombre (en minuscula), las 2 ultimas
letras del apellido (en mayusculas) y un numero que será igual a la edad de la persona al 31 de diciembre
de 2019 .-
Ejemplo: Juan Perez 1999 === >> jEZ20
"""
nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
nacimiento = int(input("Ingrese el año de nacimiento de la persona (AAAA): "))

code = ""

MAX_AGE = 2019

for item in nombre:
    if len(code) == 0 or code == "":
        code = code + item.lower()

apellido_aux = ""

for item in apellido:
    if len(apellido_aux) >= (len(apellido) - 2):
        code = code + item.upper()
    else:
        apellido_aux = apellido_aux + item

code = code + str(MAX_AGE - nacimiento)

print(nombre, " ", apellido, " ", nacimiento, ": ", code)
