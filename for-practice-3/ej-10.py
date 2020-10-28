'''
Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en
pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n
'''

number_n = int(input("Choose a number n: "))
for item in range(1, number_n):
    print(number_n * item)