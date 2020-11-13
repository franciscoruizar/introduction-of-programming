'''
Denir una función llamada sonFactores que tome un entero n y una lista de enteros, y
devuelva True si los números de la lista son factores de n (es decir, si n es divisible por todos
ellos).

'''

def son_factores(numero_entero, lista_enteros):
    for item in lista_enteros:
        if item % numero_entero != 0:
            return False
    return True

lista = [4, 5, 8, 8, 2]
number = 2

if son_factores(number, lista):
    print("Son factores")
else:
    print("No son factores")



