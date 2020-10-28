tope = int(input("Ingrese el tope deseado: "))

sum = 0
item = 1
while sum <= tope:
    item = item + 1
    sum = sum + (1/item)


print("Suma: ", item)
print("Cantidad de terminos: ", item)

'''
VALORES INICIALES
tope = 3
sum = 0
item = 1

PRUEBA DE ECRITORIO

| tope | sum | item | sum <= tope
    3     0     1         True
'''
