number = int(input("Elegir cuántos términos: "))
item = 1

acum = 0
while item < number:
    if item % 2 == 0:
        acum = acum - (1 / item )
    else:
        acum = acum + (1 / item )
    item += 1
print(acum)