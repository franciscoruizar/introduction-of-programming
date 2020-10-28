'''
a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
siguen al 10 (11, 12, · · · , 15).
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
c) Hacer un programa que permita al usuario elegir un número n y un número c, y
luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
'''

for item in range(10, 16):
    print(item)

number_n = int(input("Choose a number n: "))

for item in range(number_n, number_n + 6):
    print(item)

number_n = int(input("Choose a number n: "))
number_c = int(input("Choose a number c: "))

for item in range(number_n, number_c):
    print(item)