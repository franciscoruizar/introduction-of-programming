'''
Ejercicio 1 F

a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
(1, 2, 3, 4 y 5).

b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
primeros n números naturales (1, 2, · · · , n).

'''

i = 1
while i <= 5:
    print("Number:", i)
    i = i + 1

number = int(input("Choose a number: "))

if number >= 1 and number <= 5:
    print("Your number is ", number)
else:
    print("Your number is less or equal that 1 or more or equaoñ that 5")