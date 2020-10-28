'''
Arnaldito falto a clases cuando la maestra explico la regla ortográfica que dice que “antes de b o p
va m (y no n). Como siempre se olvida nos pidió que hagamos un programa para revisar y mostrar
la frase en forma correcta.
Ejemplo:
Frase: En dicienbre canbiaremos las computadoras, y conpraremos un conpresor nuevo.
corregida: En diciembre cambiaremos las computadoras, y compraremos un compresor nuevo.
'''

sentece = input("Ingrese su frase a corregir: ")
sentece.lower()
sentece = sentece.replace('np', 'mp')
sentece = sentece.replace('nb', 'mb')
print("Frase corregida: ", sentece)


frase = input("Ingrese frase: ")
frase = frase.lower()
print("original: ", frase)
nueva = ""
letraAnt = ""
for letraAct in frase:
    if letraAnt+letraAct == "nb" or letraAnt+letraAct == "np":
        letraAnt = "m"
    nueva = nueva+letraAnt
    letraAnt = letraAct
nueva = nueva+letraAnt        # agrego la ultima letra
print("correcta: ", nueva)
