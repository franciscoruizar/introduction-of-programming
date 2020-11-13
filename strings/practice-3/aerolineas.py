aerolinea = input("Ingrese el nimbre de la aerolinea: ")
aerolinea = aerolinea.lower()

code = ""
code_1 = ""

for item in aerolinea:
    if len(code) == 0:
        code = code + item.upper()
    else:
        if item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u':
            code_1 = item
        if code_1 == "" and not(code):
            code_1 = item
        if item == " " and code_1:
            code


print("El codigo de la aerolinea es: ", code + code_1)
