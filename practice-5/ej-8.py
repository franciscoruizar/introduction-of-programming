'''
Hacer una función que tome una lista de números decimales y devuelva el promedio de los
elementos.
'''

def promedio(numeros):
    acumulador = 0
    for item in numeros:
        acumulador += item
    return acumulador / len(numeros)

lista = [2.5, 3.8, 4, 5, 10]

print("Promedio: ", promedio(lista))