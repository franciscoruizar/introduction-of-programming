'''
generar clave .
Hacer un programa que solicite el ingreso de el nombre, el apellido y el año de nacimiento de una persona.
Generar una clave provisoria de la sig.forma: La primera letra del nombre (en minuscula), las 2 ultimas
letras del apellido (en mayusculas) y un numero que será igual a la edad de la persona al 31 de diciembre
de 2019 .-
Ejemplo: Juan Perez 1999 === >> jEZ20
'''

name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su ano de nacimiento (AAAA): ",))

max_age = 2019

if len(name) > 0 and len(lastname) > 0 and age <= max_age:
    code = ""

    code = code + name[0].lower()
    code = code + lastname[len(lastname) - 2].upper() + \
        lastname[len(lastname) - 1].upper()
    code = code + str(max_age - age)

    print(name, " ", lastname, " ", age, ": ", code)

else:
    print("Los datos ingresados fueron erroneos")
