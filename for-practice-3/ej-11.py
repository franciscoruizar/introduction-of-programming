'''
Hacer un programa que reciba un número m y determine el primer n para el cual la suma
1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 =
10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11
'''

number_m = int(input("Choose a number m: "))

acumulator = 0
item = 1
while acumulator < number_m:
    acumulator += item
    item += 1

print(acumulator)

acumulator = 0
for item in range(1 , number_m):
    if acumulator < number_m:
        acumulator += item
print(acumulator)
