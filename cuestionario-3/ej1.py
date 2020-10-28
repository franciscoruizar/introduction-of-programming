terms = int(input("Ingrese la cantidad de terminos: "))
serie = 0
numerador = 1

if terms > 0:
    for item in range(1, terms + 1):
        if item % 2 == 0:
            serie = serie - (numerador / item ** 2)
        else:
            serie = serie + (numerador / item ** 2)

        numerador = numerador + 2

    print("La serie para", terms, " en terminos es: ", serie)
else:
    print("Su numero debe ser mayor a 0")

'''
VALORES INICIALES
terms = 6
serie = 0

PRUEBA DE ECRITORIO

  terms > 0  | terms |       serie     | item | numerador | range(1, terms + 1) | if item % 2 == 0 | numerador / item ** 2
      True      6             1           1        1              True                  False          + 1 / 1 ** 2 
                6           0.25          2        3              True                  True           - 3 / 2 ** 2
                6    0.8055555555555556   3        5              True                  False          + 5 / 3 ** 2
                6    0.3680555555555556   4        7              True                  True           - 7 / 4 ** 2
                6    0.7280555555555556   5        9              True                  False          + 9 / 5 ** 2
                6          0.4225         6        11             True                  True           - 11 / 6 ** 2

VALORES FINALES

terms = 6
serie = 0.4225

'''
