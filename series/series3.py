# SERIES. calcular la serie para un numero de teminosindicado por el usuario
# S= 1 - 1 / 2 + 1 / 3 - 1 / 4 + .......
print("calcula la serie  S= 1 - 1 / 2 + 1 / 3 - 1 / 4 + .........")
s = 0
n = int(input("cantidad de terminos"))

signo = 1
for i in range(1, n+1):
    s = s + 1 / i * signo
    signo = signo*(-1)

print("la serie para", n, "terminos es:", s)
