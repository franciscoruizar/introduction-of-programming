"""
En las pantallas de Partidasy Llegadas de vuelos de los aeropuertos, se asigna una abreviatura a cada
vuelo compuesta por dos letras que identifican a cada aerolínea. Se le pide codificar la determinación de la
abreviatura correspondiente a cada aerolínea respetando las siguientes pautas:
Ambas letras se muestran en mayúsculas.
Si el nombre de la aerolínea es una sola palabra la abreviatura se formará con la primera letra más la
siguiente consonante.
Si el nombre de la aerolínea consta de dos palabras, la abreviatura se formará con la primera letra de
cada palabra.
Ejemplos: Aerolíneas  AR Emirates  EM TAM  TM Gol GL IBERIA  IB
Ejemplos: Air France  AF American Airlines  AA United Airlines  UA
El programa deberá solicitar el ingreso del nombre de la aerolínea y mostrar la abreviatura generada.

"""

aerolinea = input("Ingrese la aerolinea: ")

code = ""
letra_aux = ""
consonante_aux = ""
aerolinea = aerolinea.lower()

for item in aerolinea:
    if len(code) == 0 or code == "":
        code = code + item.upper()
    elif letra_aux == " ":
        code = code + item.upper()
    elif consonante_aux == "" and item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
        consonante_aux = item
    letra_aux = item

if len(code) == 1:
    code = code + consonante_aux.upper()

print("El codigo es: ", code)
