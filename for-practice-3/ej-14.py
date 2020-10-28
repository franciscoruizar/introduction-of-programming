import math

print(math.log(2))

number = int(input("Elegir cuántos términos: "))
sign = 1
acum = 0
for item in range(1, number + 1):
    acum += 1 / item * sign
    sign = sign * (-1)
print("La serie para", number, "teminos es", acum)