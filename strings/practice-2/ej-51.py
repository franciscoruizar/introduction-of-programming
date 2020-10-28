'''
Hacer un programa que solicite el título de un libro y la cantidad de páginas. Debe informar uncódigo para
regfistro en el catálogo de la biblioteca formado por las iniciales de cada una de las palabras del título,
altermando una mayúscula y una minúscula (comenzando con mayúscula), Ejemplo:
título = “Del Imperio al Desamparo”
debe mostrar: “El codigo del libro Del Imperio al Desamparo es DiAd”
'''

title = input("Ingrese el título del libro: ")

words = title.split(" ")

code = ""
is_last_letter_mayus = False
for item in words:

    letter = item[0]

    if is_last_letter_mayus:
        code = code + letter.lower()
    else:
        code = code + letter.upper()

    is_last_letter_mayus = not is_last_letter_mayus

print("El código del libro es: ", code)
