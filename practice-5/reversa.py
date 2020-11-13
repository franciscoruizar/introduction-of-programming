def reverse(a):
    midpoint = len(a)/2
    for item in a[:midpoint]:
        otherside = (len(a) - a.index(item)) - 1
        temp = a[otherside]
        a[otherside] = a[a.index(item)]
        a[a.index(item)] = temp
    return a

            

numeros = [2, 3, 4, 11, 10]

print(numeros)
print(reverse(numeros))
