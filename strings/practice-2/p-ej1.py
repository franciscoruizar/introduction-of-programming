"""
Cadenas – Generar claves
Hacer un programa que genere claves provisorias para cada usuario, siguiendo
las siguientes reglas:
Longitud 8 caracteres, formada por la primera letra del nombre + las 3 últimas
cifras del año de nacimiento + las consonantes del apellido hasta completar la
longitud de la clave; si no llega a la longitud, completar con “A” (letras A).
Ejemplo: Juan Fernandez 2003 CLAVE: J003frnn
"""

nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
nacimiento = int(input("Ingrese el año de nacimiento de la persona (AAAA): "))

CANT_CARACTERES = 8
CANT_CIFRAS_NACIMIENTO = 3
LETRA_RESTANTE = 'A'

code = ""

for item in nombre:
    if len(code) == 0 or code == "":
        code = code + item.upper()

primera_letra = True
for item in str(nacimiento):
    if primera_letra:
        primera_letra = not primera_letra
    else:
        code = code + item

for item in apellido:
    if len(code) < CANT_CARACTERES and (item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u'):
        code = code + item.lower()

if len(code) < CANT_CARACTERES:
    code = code + (LETRA_RESTANTE * (CANT_CARACTERES - len(code)))

print("El codigo para la persona ", nombre, " ", apellido, "es: ", code)
