tope = int(input("Ingrese el tope deseado: "))

multiplo = 5
item = 1
sum = 0
while sum <= tope:
    sum = sum + (multiplo * item)

    if sum <= tope:
        item = item + 1

print(item)
