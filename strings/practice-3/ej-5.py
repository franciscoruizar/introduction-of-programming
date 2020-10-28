"""
1)Verificar clave:
El banco Bb, por razones de seguridad solicita que las claves que utilicen sus clientes tengan: una
longitud mínima de 6 caracteres, incluyendo al menos 1 letra minúscula, 1 letra mayúscula y 1
numero.
Hacer un programa que verifique si la clave es valida como clave.
Ejemplos :
clave1="H3C_2A8" #invalida no tiene minusculas
clave2="325FFG*j" #valida
clave3="hGhK-p" #invalida no tiene numeros
clave4="2Am" #invalida demasiado corta
"""

password = input("Ingrese su contrase: ")

CANT_MAX_CARACTERES = 6
CANT_MAX_MAYUS = 1
CANT_MAX_MINUS = 1
CANT_MAX_NUMBS = 1

if len(password) >= CANT_MAX_CARACTERES:
    cant_mayus = 0
    cant_minus = 0
    cant_numbs = 0

    for item in password:
        if item >= 'a' and item <= 'z':
            cant_minus = cant_minus + 1
        elif item >= 'A' and item <= 'Z':
            cant_mayus = cant_mayus + 1
        elif item >= '1' and item <= '9':
            cant_numbs = cant_numbs + 1

    if cant_mayus == CANT_MAX_MAYUS:
        print("Su password no contine las suficientes letras mayusculas")
    elif cant_minus == CANT_MAX_MINUS:
        print("Su password no contine las suficientes letras minusculas")
    elif cant_numbs == CANT_MAX_NUMBS:
        print("Su password no contine los suficiente numeros")
    else:
        print("Su password es segura")
else:
    print("Su password tiene menos de ", CANT_MAX_CARACTERES, " car")
