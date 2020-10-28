'''
El banco Bb, por razones de seguridad solicita que las claves que utilicen sus clientes tengan: una
longitud mínima de 6 caracteres, incluyendo al menos 1 letra minúscula, 1 letra mayúscula y 1
numero.
Hacer un programa que verifique si la clave es valida como clave.
Ejemplos :
clave1="H3C_2A8" #invalida no tiene minusculas
clave2="325FFG*j" #valida
clave3="hGhK-p" #invalida no tiene numeros
clave4="2Am" #invalida demasiado corta
'''

password = input("Ingrese su contraseña: ")

MAX_CHARACTERS = 6
MIN_MINUS_LETTERS = 1
MIN_MAYUS_LETTERS = 1
MIN_NUMBERS = 1

response = ""

if len(password) >= MAX_CHARACTERS:
    minus_letters = 0
    mayus_letter = 0
    numbers = 0

    for item in password:
        if item >= 'a' and item <= 'z':
            minus_letters += 1
        elif item >= 'A' and item <= 'Z':
            mayus_letter += 1
        elif item >= '1' and item <= '9':
            numbers += 1

    if minus_letters < MIN_MINUS_LETTERS:
        response += ". No tiene las suficientes minusculas\n"
    elif mayus_letter < MIN_MAYUS_LETTERS:
        response += ". No tiene las suficientes mayusculas\n"
    elif numbers < MIN_NUMBERS:
        response += ". No tiene sufucientes numeros\n"
    else:
        response += "Contraseña valida"
else:
    response = ". Contraseña demasiada corta\n"

print(response)
