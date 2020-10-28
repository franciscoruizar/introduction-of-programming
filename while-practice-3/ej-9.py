number_c = int(input("Numero: "))
number_n = int(input("Cantidad de divisores: "))


item = number_c
count = 0
while count < number_n:
    if (number_c % item == 0):
        print("Divisor: ", item)
        count += 1
    item -= 1