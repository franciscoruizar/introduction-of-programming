'''
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4,
6...
b) Idem anterior para la sucesión an = 2n − 1.
c) Idem anterior para la sucesión an = n
2
.
d) Idem anterior para la sucesión an = n
3 − n
2
.
e) Idem anterior para la sucesión an =
1
n2 .
'''

number_n = int(input("Choose a number n: "))

#A
for item in range(2, number_n + 1):
    print(2 * item)

#B
for item in range(1, number_n +1):
    print(2 * item - 1)

#C
for item in range(1, number_n + 1):
    print(item ** 2)

#D
for item in range(1, number_n + 1):
    print(item ** 3 - item ** 2)

#E
for item in range(1, number_n + 1):
    print(1/ (item**2))
