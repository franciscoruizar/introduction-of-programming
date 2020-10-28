'''
a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el
11 salteando de a 2 elementos (5, 7, 9 y 11)

b) Hacer un programa que permita al usuario elegir un número m y un n y luego
muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el
usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar
2, 5, 8, 11, 14.

c) Hacer un programa que permita al usuario elegir un número n, un m y un p y
luego muestre todos los naturales entre m y n, pero salteando de a p números. Por
ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4,
el programa deberá mostrar 2, 6, 10, 14.
'''

item = 5
MAX_NUM = 11
while item <= MAX_NUM:
    print(item)
    item = item + 2

number_n = int(input("Choose a number: "))
number_m = int(input("Choose another number: "))
MAX_NUM = 3

while number_n <= number_m:
    print(number_n)
    number_n = number_n + MAX_NUM

number_n = int(input("Choose a number: "))
number_m = int(input("Choose another number: "))
number_p = int(input("Choose other number: "))

while number_n <= number_m:
    print(number_n)
    number_n = number_n + number_p
