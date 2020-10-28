'''
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
7 (4, 5, 6 y 7).

b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
si n es menor que m?
'''

for item in range(4, 7 + 1):
    print(item)

number_m = int(input("Choose a number m: "))
number_n = int(input("Choose a number n: "))

for item in range(number_m, number_n):
    print(item)