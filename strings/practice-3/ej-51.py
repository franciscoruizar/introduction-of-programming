"""
Ej 51.-Código libtro.
Hacer un programa que solicite el título de un libro y la cantidad de páginas. Debe informar uncódigo para
regfistro en el catálogo de la biblioteca formado por las iniciales de cada una de las palabras del título,
altermando una mayúscula y una minúscula (comenzando con mayúscula), Ejemplo:
título = “Del Imperio al Desamparo”
debe mostrar: “El codigo del libro Del Imperio al Desamparo es DiAd”
"""

titulo = input("Ingrese el titulo del libro: ")
cant_pags = input("Ingrese la cant de pags del libro: ")

letra_anterior = ""
code = ""
for item in titulo:
    if len(code) == 0 or code == "":
        code = code + item.upper()
    elif letra_anterior == " ":
        if len(code) % 2 == 0:
            code = code + item.upper()
        else:
            code = code + item.lower()
    letra_anterior = item

print("El codigo del libro ", titulo, "es: ", code)
