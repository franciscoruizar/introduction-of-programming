class FileRepository():

    def __init__(self):
        self.ARCHIVO = "numeros.txt"

    def remove_space(self, element):
        return element[:-1]

    def find_all(self):
        numbers = open(self.ARCHIVO, "r")

        response = []

        for item in numbers:
            item = self.remove_space(item)
            response.append(item)

        numbers.close()

        return response

    def count(self):
        numbers = open(self.ARCHIVO, "r")

        response = len(numbers.readlines())

        numbers.close()

        return response

    def is_exists(self, element):
        file = open(self.ARCHIVO, "r")

        numbers = file.readlines()

        response = False

        for item in numbers:
            if self.remove_space(item) == str(element):
                response = True

        file.close()

        return response

    def write(self, element):
        numbers = open(self.ARCHIVO, "a")

        numbers.write(str(element) + "\n")
            
        numbers.close()

    def write_list(self, elements):
        numbers = open(self.ARCHIVO, "a")

        for item in elements:
            numbers.write(str(item) + "\n")

        numbers.close()