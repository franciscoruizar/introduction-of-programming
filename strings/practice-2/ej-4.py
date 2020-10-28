'''
Hacer un programa que reciba una palabra e indique si en la misma hay 2 vocales seguidas.
Ejemplo:
palabra=”Bahia” >> La palabra Bahia SI tiene 2 vocales seguidas.
palabra=”ciudad” >> La palabra ciudad SI tiene 2 vocales seguidas.
palabra=”zoologico” >> La palabra zoologico SI tiene 2 vocales seguidas.
'''

word = input("Ingrese una palabra: ")
number_of_vowels = 2

is_last_letter_vocal = False
vowel = 0
for item in word:
    if item.casefold() in 'aeiou':
        vowel += 1
        is_last_letter_vocal = True
    else:
        is_last_letter_vocal = False
        vowel = 0

if is_last_letter_vocal and vowel == number_of_vowels:
    print("Tiene dos vocales seguidas")
else:
    print("No tiene dos vocales seguidas")
