'''
Hacer un programa que reciba una frase y muestre la palabra más larga (si hubiera 2 (o más) de igual largo
que resultaran ser las más largas, mostrar cualquiera de ellas).
Ejemplo:
frase=”Nos los representantes de la Nacion Argentina”
debe mostrar:
la palabra más larga es representantes
'''

frase = input("Ingrese su frase: ")

palabras = frase.split(" ")

palabra_larga = ""
for item in palabras:
    if len(item) > len(palabra_larga):
        palabra_larga = item

print(palabra_larga)
