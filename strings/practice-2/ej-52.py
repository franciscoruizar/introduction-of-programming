"""
Ej 52.-Código Autor.
Hacer un programa que solicite el nombre y apellido del autor de un libro y genere un código para el mismo
tomando la primera letra del nombre (en minúcula), seguido del caracter “_” (subraya), más la Primera
letra del apellido (en mayúscula) y las sguientes 3 consonantes del apellido (en minúsculas); si no hubiera
suficientes debera completarse con letras “A”.
Ejemplos:
- autor Domingo Sarmiento
debe mostrar: para el autor Domingo Sarmiento el codigo es: d_Srmn
- autor Juan Paso
debe mostrar: “para el autor Juan Paso el codigo es: j_PsAA”

"""

nombre = input("Ingrese el nombre del autor: ")
apellido = input("Ingrese el apellido del autor: ")

code = ""
CANT_CARACTERES = 6
LETRA_RESTANTE = 'A'

for item in nombre:
    if len(code) == 0 or code == "":
        code = code + item.upper() + "_"

for item in apellido:
    if len(code) < CANT_CARACTERES:
        if len(code) == 2:
            code = code + item.upper()
        elif item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
            code = code + item.lower()

if len(code) < CANT_CARACTERES:
    code = code + (LETRA_RESTANTE * (CANT_CARACTERES - len(code)))

print("El codigo para el autor ", nombre, " ", apellido, "es: ", code)
