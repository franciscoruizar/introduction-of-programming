'''
Escribir una función llamada maximoIndice que tome una lista de números y devuelva el
índice del máximo elemento.
'''

def maximo_indice(numeros):
    maximo_indice = None
    for item in range(0, len(numeros)):
        if maximo_indice == None or numeros[item] > maximo_indice:
            maximo_indice = item

    return maximo_indice


lista = [2.5, 3.8, 4, 11, 10]

print("Maximo: ", maximo_indice(lista))

lista = []

print("Maximo 2: ", maximo_indice(lista))