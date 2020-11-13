'''
Código Autor.
Hacer un programa que solicite el nombre y apellido del autor de un libro y genere un código para el mismo
tomando la primera letra del nombre (en minúcula), seguido del caracter “_” (subraya), más la Primera
letra del apellido (en mayúscula) y las sguientes 3 consonantes del apellido (en minúsculas); si no hubiera
suficientes debera completarse con letras “A”.
Ejemplos:
- autor Domingo Sarmiento
debe mostrar: para el autor Domingo Sarmiento el codigo es: d_Srmn
- autor Juan Paso
debe mostrar: “para el autor Juan Paso el codigo es: j_PsAA”
'''

name = input("Ingrese el nombre del autor: ")
lastname = input("Ingrese el apellido del autor: ")

code = ""
for item in name:
    if len(code) == 0:
        code = code + item.lower()

code = code + "_"

for item in lastname:
    if len(code) == 2:
        code = code + lastname[0].upper()
    elif len(code) == 3:
        if len(code) < 6 and not(item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u'):
            code = code + item

while len(code) < 6:
    code = code + 'A'


print("Para el autor ", name, " ", lastname, "el codigo es: ", code)
