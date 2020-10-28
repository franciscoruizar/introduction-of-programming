'''
a) Hacer un programa que reciba un número n y muestre todas las potencias de 2
menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8
16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.
b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
16 32.
c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
256. 1^1, 2^2, 3^3 ,4^4
'''

#A
number_n = int(input("Choose a number n: "))

item = 1
while item < number_n:
    print(item)
    item = item * 2

#B
number_n = int(input("Choose a number n: "))

if number_n > 2:
    count = 1
    item = 1
    while count <= number_n:
        print(item)
        item *= 2
        count += 1

#C
number_n = int(input("Choose a number n: "))
if number_n > 2:
    item = 1
    while item <= number_n:
        print(item ** item)
        item += 1