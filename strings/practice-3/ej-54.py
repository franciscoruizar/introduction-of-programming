"""
Ej 54- Las 2 palabras más largas
Hacer un programa que reciba una frase y muestre las 2 palabras más largas (si hubiera más de las
necesarias, mostrar 2 cualeslquiera de ellas).
ejemplo:
frase="Google dio a conocer una nueva herramienta de su buscador" "
debe mostrar: “Las 2 palabras mas largas son: herramienta - buscador”
"""
frase = input("Ingrese la frase: ")

palabra_larga = ""
segunda_palabra_larga = ""
palabra_actual = ""
for item in frase:
    if item == " ":
        if len(palabra_actual) > len(palabra_larga):
            palabra_larga = palabra_actual
            segunda_palabra_larga = palabra_larga
        elif len(palabra_actual) > len(segunda_palabra_larga):
            segunda_palabra_larga = palabra_actual
        palabra_actual = ""
    else:
        palabra_actual = palabra_actual + item

print("Las dos palabras mas largas son: ",
      palabra_larga, "-", segunda_palabra_larga)
