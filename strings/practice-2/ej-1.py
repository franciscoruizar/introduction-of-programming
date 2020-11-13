"""
1-Ej Palabras.
Hacer un programa que reciba una frase y muestre una a una todas las palabras que la componen.
Ejemplo:
frase=”Nos los representantes de la Nacion Argentina”
debe mostrar:
Nos
los
representenates
de
la
Nacion
Argentina

"""

frase = input("Ingrese su frase: ")

palabra = ""
for item in frase:
    if item == " ":
        print(palabra)
        palabra = ""
    else:
        palabra = palabra + item
