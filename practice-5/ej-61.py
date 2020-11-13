def clasificar_datos(datos, lista_pares, lista_impares):
    for item in range(0, len(datos)):
        if datos[item] % 2 == 0:
            lista_pares.append(item)
        else:
            lista_impares.append(item)


datos = [ 1 , 3 , 2 , 4 , 5 , 7 , 9 , 6 , 8 , 2 , 2 , 14 ,15 ,16 , 17 ]
lista_pares = []
lista_impares = []

clasificar_datos(datos, lista_pares, lista_impares)

print("Lista pares:", lista_pares)
print("Lista impares:", lista_impares)