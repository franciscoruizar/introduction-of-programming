'''
Hacer un programa que reciba una frase e indique si tiene alguna letra mayúscula.
Ejemplo:
Ushuaia es la capital de Tierra del Fuego >> la frase tiene mayúsculas.
ushuaia es la capital de tierra del fuego >> No tiene mayusculas.

'''

frase = input("Ingrese su frase: ")
mayusculas = 0
for item in frase:
    if item >= 'A' and item <= 'Z':
        mayusculas += 1

if mayusculas == 0:
    print("No tiene mayusculas")
else:
    print("Tiene mayusculas")
