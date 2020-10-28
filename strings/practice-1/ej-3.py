'''
Hacer un programa que reciba una frase e indique si tiene alguna letra mayúscula.
Ejemplo:
Ushuaia es la capital de Tierra del Fuego >> la frase tiene mayúsculas.
ushuaia es la capital de tierra del fuego >> No tiene mayusculas.t
'''

frase = input("Ingrese una frase: ")
cant_mayusculas = 0
for item in frase:
    if item >= 'A' and item <= 'Z':
        cant_mayusculas += 1
if cant_mayusculas == 0:
    print("La frase no posee mayusculas")
else:
    print("La frase tiene mayúsculas")
