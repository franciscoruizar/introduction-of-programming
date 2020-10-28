"""
2)Mini corrector ortografico:
Arnaldito falto a clases cuando la maestra explico la regla ortográfica que dice que “antes de b o p
va m (y no n). Como siempre se olvida nos pidió que hagamos un programa para revisar y mostrar
la frase en forma correcta.
Ejemplo:
Frase: En dicienbre canbiaremos las computadoras, y conpraremos un conpresor nuevo.
corregida: En diciembre cambiaremos las computadoras, y compraremos un compresor nuevo.
"""

frase = input("Ingrese su frase: ")

frase_aux = ""
letra_anterior = ""
for item in frase:
    if (letra_anterior) == 'n' and (item == 'b' or item == 'p'):
        letra_anterior = 'm'
    frase_aux = frase_aux + letra_anterior
    letra_anterior = item

frase_aux = frase_aux + letra_anterior

print("Corregido: ", frase_aux)
