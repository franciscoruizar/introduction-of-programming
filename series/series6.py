# SERIES. calcular la serie para un numero de teminos indicado por el usuario
# S= 1 + 1 / 3 + 1 / 5 + 1 / 7 + .......
print("calcula la serie  S= 1 + 1 / 3 + 1 / 5 + 1 / 7 + ........")
s = 0
n = int(input("cantidad de terminos"))

for i in range(1, 2*n, 2):
    s = s+1/i

print("la serie para", n, "terminos es:", s)
