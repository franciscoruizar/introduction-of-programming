'''
Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta
el 6 pero salteando de a tres (15, 12, 9, 6).
'''
start = 15
stop = 6
step = -3

for item in range(start, stop - 1, step):
    print(item)