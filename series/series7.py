# SERIES. calcular la serie para un numero de teminos indicado por el usuario
# S= 1 / 2 - 2 / 3**2 + 3 / 4**3 - 4 / 5**4 + .......
print("calcula la serie   S= 1 / 2 - 2 / 3**2 + 3 / 4**3 - 4 / 5**4 + .......")
s = 0
n = int(input("cantidad de terminos"))
signo = 1
for i in range(1, n+1):

    s = s+i/(i+1)**i * signo
    signo = signo*(-1)

print("la serie para", n, "terminos es:", s)
