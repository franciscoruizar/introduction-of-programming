'''
Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modicar la que
toma como parámetro.
'''

def intercambiar(numeros, a, b):
    if (a > 0 and b > 0) and (a < len(numeros) and b < len(numeros)):
        numero_backup = numeros[a]
        numeros[a] = numeros[b]
        numeros[b] = numero_backup


numeros = [2, 3, 4, 11, 10]
a = 1
b = 2
print(numeros)
intercambiar(numeros, a, b)
print(numeros)
