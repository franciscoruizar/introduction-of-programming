'''
Ejercicio 3 F

a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le
siguen al 10 (11, 12, · · · , 15).
b) Hacer un programa que permita al usuario elegir un número n y luego muestre los
5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).
c) Hacer un programa que permita al usuario elegir un número n y un número c, y
luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).

'''
iterator = 10
while iterator <= 15:
    print("Number:", iterator)
    iterator = iterator + 1

#################################################3

number = int(input("Choose a number: "))
iterator = 1
MAX_NUMBERS = 5

while iterator <= MAX_NUMBERS:
    print("Number:", number + iterator)
    iterator = iterator + 1

##################################################

number_n = int(input("Choose a number: "))
number_c = int(input("Choose a other number: "))

iterator = 1
while iterator <= number_c:
    print("Number "+ str(number_n) +" + " + str(iterator) +":" + str(number_n + iterator))
    iterator = iterator + 1
