number_m = int(input("Eleja un número: "))

sum = 0
item = 1
while sum <= number_m:
    item += 1
    sum = sum + item

print(item)


'''
| sum | item | sum <= number_m
   0     1           True
   1     2           True
   3     3           True
   6     4           True
   10    5           True
'''