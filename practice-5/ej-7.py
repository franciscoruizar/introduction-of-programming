'''
Denir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
hace, y -1 en caso contrario.
'''

def donde_aparece(numeros, blanco):
    for item in range(0, len(numeros)):
        if numeros[item] == blanco:
            return item
    return -1

lista = [2, 3, 4, 5, 10]
numero = 10

ubicacion = donde_aparece(lista, numero)

if ubicacion == -1:
    print("El numero no aparece")
else:
    print("El numero aparece en la posicion ", ubicacion + 1)