def verificar_numero(numero, numero_comparar):
    return numero_comparar == numero


def recorrer_verficar_lista(lista, numero):
    for item in lista:
        if isinstance(item, list):
            for subitem in item:
                if verificar_numero(subitem, numero):
                    return True
        else:
            if verificar_numero(item, numero):
                return True
    return False


numero = 99
datos = [[15, 38, 28, 45], [10, 30, 22, 47], [16, 32, 5, 8], 99]

if recorrer_verficar_lista(datos, numero):
    print("EL numero", numero, "está en la lista")
else:
    print("EL numero", numero, "NO está en la lista")
