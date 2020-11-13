'''
Las 2 palabras más largas
Hacer un programa que reciba una frase y muestre las 2 palabras más largas (si hubiera más de las
necesarias, mostrar 2 cualeslquiera de ellas).
ejemplo:
frase="Google dio a conocer una nueva herramienta de su buscador" "
debe mostrar: “Las 2 palabras mas largas son: herramienta - buscador”
'''

frase = input("Ingrese su frase: ")

palabra_1 = ""
palabra_2 = ""

palabras = frase.split(" ")

for item in palabras:
    if len(item) >= len(palabra_1):
        palabra_2 = palabra_1
        palabra_1 = item
    elif len(item) >= len(palabra_2):
        palabra_2 = item

print(palabra_1, "-", palabra_2)
