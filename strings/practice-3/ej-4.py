"""
4- Hacer un programa que reciba una palabra e indique si en la misma hay 2 vocales seguidas.
Ejemplo:
palabra=”Bahia” >> La palabra Bahia SI tiene 2 vocales seguidas.
palabra=”ciudad” >> La palabra ciudad SI tiene 2 vocales seguidas.
palabra=”zoologico” >> La palabra zoologico SI tiene 2 vocales seguidas
"""

palabra = input("Ingrese una palabra: ")

letra_anterior = ""
tiene_vocales_seguidas = False
for item in palabra:
    if (item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'u') and (letra_anterior == 'a' or letra_anterior == 'e' or letra_anterior == 'i' or letra_anterior == 'o' or letra_anterior == 'u'):
        tiene_vocales_seguidas = True
    letra_anterior = item

definicion = "NO"
if tiene_vocales_seguidas:
    definicion = "SI"

print("La palabra ", palabra, " ", definicion, " tiene dos vocales seguidas")
