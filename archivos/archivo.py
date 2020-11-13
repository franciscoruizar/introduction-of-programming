ARCHIVO = "numeros.txt"

def remove_space(element):
    return element[:-1]

def find_all():
    numbers = open(ARCHIVO, "r")

    response = []

    for item in numbers:
        item = remove_space(item)
        response.append(item)

    numbers.close()

    return response

def is_exists(element):
    file = open(ARCHIVO, "r")

    numbers = file.readlines()

    for item in numbers:
        if remove_space(item) == str(element):
            return True

    file.close()

    return False

def write(element):
    numbers = open(ARCHIVO, "a")

    numbers.write(str(element) + "\n")
        
    numbers.close()

def write_list(elements):
    numbers = open(ARCHIVO, "a")

    for item in elements:
        numbers.write(str(item) + "\n")

    numbers.close()

write(5)
print(find_all())