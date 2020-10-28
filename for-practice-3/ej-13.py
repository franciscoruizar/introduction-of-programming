'''
a) Hacer un programa que permita al usuario elegir un número positivo n y luego
muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir,
2 6 12 20...
b) Idem anterior para la sucesión an = n
2
.
c) Idem anterior para la sucesión an = n
3 − n
2
.
d) Idem anterior para la sucesión an =
1
n2 .
e) ¾A qué valor se va acercando la suma del inciso anterior a medida que utilizamos
un valor alto de n?
'''

number_n = int(input("Choose a number n: "))

#A
sum = 0
for item in range(1, number_n):
    sum += 2 * item
    print(sum)
    
#B
sum = 0
for item in range(1, number_n):
    sum += item ** 2
    print(sum)

#C
sum = 0
for item in range(1, number_n):
    sum += item**3 - item**2
    print(sum)

#D
sum = 0
for item in range(1, number_n):
    sum += 1/(item**2)
    print(sum)