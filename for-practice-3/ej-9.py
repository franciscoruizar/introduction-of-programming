'''
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores de n.
b) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla todos los divisores pares de n.
c) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla la cantidad de divisores de n.
d) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla la suma de los divisores de n.
e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los primeros c divisores de n.
f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
muestre en pantalla los últimos c divisores de n.
'''
#A
number_n = int(input("Choose a number n: "))

for item in range(1, number_n + 1):
    if number_n % item == 0:
        print(item)

#B
number_n = int(input("Choose a number n: "))
for item in range(1, number_n + 1):
    if number_n % item == 0:
        if item % 2 ==0:
            print(item)

#C
number_n = int(input("Choose a number n: "))
cant_divisor = 0
for item in range(1, number_n + 1):
    if number_n % item == 0:
        cant_divisor += 1
print(cant_divisor)

#D
number_n = int(input("Choose a number n: "))
sum_divisors = 0
for item in range(1, number_n + 1):
    if number_n % item == 0:
        sum_divisors += item
print(sum_divisors)

#E
number_c = int(input("Choose a number c: "))
number_n = int(input("Choose a number n: "))

for item in range(1, number_n):
    if number_c % item == 0:
        print(item)

#F
number_c = int(input("Choose a number c: "))
number_n = int(input("Choose a number n: "))

for item in range(number_n, 1, -1):
    if number_c % item == 0:
        print(item)