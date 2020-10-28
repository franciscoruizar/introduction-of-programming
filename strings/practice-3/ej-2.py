"""
2- Ej Palabra más larga
Hacer un programa que reciba una frase y muestre la palabra más larga (si hubiera 2 (o más) de igual largo
que resultaran ser las más largas, mostrar cualquiera de ellas).
Ejemplo:
frase=”Nos los representantes de la Nacion Argentina”
debe mostrar:
la palabra más larga es representantes
"""

frase = input("Ingrese su frase: ")

palabra_larga = ""
palabra_actual = ""
for item in frase:
    if item == " ":
        if len(palabra_actual) >= len(palabra_larga):
            palabra_larga = palabra_actual
            palabra_actual = ""
    else:
        palabra_actual = palabra_actual + item

print("La palabra mas larga es: ", palabra_larga)
