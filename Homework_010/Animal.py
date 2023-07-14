# Создано три (или более) отдельных классов животных.
# Например птицы, рыбы, рептилии т.д.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создан метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, area):
        self.area = area


class Fishes(Animal):
    def __init__(self, area, add_info):
        self.add_info = add_info
        super().__init__(area)


        def __str__(self):
            return f'{type(self).__name__} area = {self.area} info: {self.add_info}'


class Birds(Animal):
    def __init__(self, area, wings):
        self.wings = wings
        super().__init__(area)


    def __str__(self):
        return f'{type(self).__name__} area = {self.area} info: {self.wings}'


class Reptiles(Animal):


    def __init__(self, area, info):
        self.info = info
        super().__init__(area)


    def __str__(self):
        return f'{type(self).__name__} area = {self.area} info: {self.info}'


if __name__ == '__main__':
    d = Reptiles("river", "crocodile")
    print(d)