number = int(input("Elija un número: "))

item = 1
sum = 0
while item <= number:
    sum = sum + (2 * item)
    item += 1
    print(sum)

number = int(input("Elija un número: "))

item = 1
sum = 0
while item <= number:
    sum = sum + (item**2)
    item += 1
    print(sum)

number = int(input("Elija un número: "))

item = 1
sum = 0
while item <= number:
    sum = sum + (item**3 - item**2)
    item += 1
    print(sum)

number = int(input("Elija un número: "))

item = 1
sum = 0
while item <= number:
    sum = sum + (1 / (item**2))
    item += 1
    print(sum)