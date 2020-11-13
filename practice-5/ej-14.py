def interseccion(list1, list2):
    response = []
    for item in list1:
        for subitem in list2:
            if subitem == item:
                response.append(subitem)
    return response

def union(list1, list2):
    return list1.extend(list2)

list1 = [ 5, 2, 48, 6, 8, 9, 10, 4]
list2 = [ 2, 5, 6, 7, 9, 15, 10, 8]
print(list1)
print(list2)
print("La lista de interseccion es:",interseccion(list1, list2))
print("La lista de union es:",union(list1, list2))
