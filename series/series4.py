# SERIES. calcular la serie para un numero de teminos indicado por el usuario
# S= 1 - 1 / 2 + 1 / 3 - 1 / 4 + .......
print("calcula la serie  S= 1 - 1 / 2 + 1 / 3 - 1 / 4 + .........")
s = 0
n = int(input("cantidad de terminos"))

for i in range(1, n+1):
    s = s + 1 / i * (-1)**(i+1)

print("la serie para", n, "terminos es:", s)
