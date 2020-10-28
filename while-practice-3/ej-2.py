'''

Ejercicio 2 F
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el
7 (4, 5, 6 y 7).

b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¾Qué pasa
si n es menor que m?

'''
iterator = 4
while iterator <= 7:
    print("Number:", iterator)
    iterator = iterator + 1

number_m = int(input("Choose a number: "))
number_n = int(input("Choose a other number: "))

if number_m <= number_n:
    iterator = number_m
    while iterator <= number_n:
        print("Number:", iterator)
        iterator = iterator + 1
else:
    iterator = number_n
    while iterator <= number_m and iterator >= 0:
        print("Number:", iterator)
        iterator = iterator + 1