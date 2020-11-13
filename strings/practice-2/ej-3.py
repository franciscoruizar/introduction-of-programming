"""
3- Tiene mayúsculas
Hacer un programa que reciba una frase e indique si tiene alguna letra mayúscula.
Ejemplo:
Ushuaia es la capital de Tierra del Fuego >> la frase tiene mayúsculas.
ushuaia es la capital de tierra del fuego >> No tiene mayusculas.
"""

frase = input("Ingrese su frase: ")

tiene_mayus = False
for item in frase:
    if item >= 'A' and item <= 'Z':
        tiene_mayus = True

if tiene_mayus:
    print("La frase tiene mayusculas")
else:
    print("La frase no tiene mayusculas")
