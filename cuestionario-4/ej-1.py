nombre = input("Ingrese el nombre de la persona: ").lower()
apellido = input("Ingrese el apellido de la persona: ").lower()


code = ""
consonantes_nombre = ""
vocales_nombre = ""

consonantes_apellido = ""
vocales_apellido = ""

for item in nombre:
    if item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
        consonantes_nombre = consonantes_nombre + item
    else:
        vocales_nombre = vocales_nombre + item


for item in apellido:
    if item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
        consonantes_apellido = consonantes_apellido + item
    else:
        vocales_apellido = vocales_apellido + item


if len(consonantes_apellido) >= len(consonantes_nombre):
    consonantes_invertidos = ""
    for item in consonantes_apellido:
        consonantes_invertidos = item + consonantes_invertidos

    code = code + consonantes_invertidos

    code = code + vocales_nombre
    code = code + str(len(vocales_apellido) + len(consonantes_nombre))
else:

    consonantes_invertidos = ""
    for item in consonantes_nombre:
        consonantes_invertidos = item + consonantes_invertidos

    code = code + consonantes_invertidos

    code = code + vocales_apellido
    code = code + str(len(vocales_nombre) + len(consonantes_apellido))


print("El codigo para ", nombre, " ", apellido, "es: ", code.upper())
