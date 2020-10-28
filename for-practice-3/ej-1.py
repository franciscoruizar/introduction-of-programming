'''
a) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales
(1, 2, 3, 4 y 5).

b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
primeros n números naturales (1, 2, · · · , n).
'''

for item in range(1, 6):
    print(item)

number = int(input("Choose a number: "))

for item in range(1, number + 1):
    print(item)

