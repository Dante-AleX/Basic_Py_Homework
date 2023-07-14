# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

# from Animal import Birds, Reptiles, Fishes


# class AnimalFabric:
#     def make_animal(self, animal_type: str, *args, **kwargs):
#         new_animal = self._get_maker(animal_type)
#         return new_animal(*args, **kwargs)

#     def _get_maker(self, animal_type: str):
#         types = {"bird": Birds, "reptile": Reptiles, "fish": Fishes}
#         return types[animal_type.lower()]


# if __name__ == '__main__':
#     fabric = AnimalFabric()
#     animal_from_fabric = fabric.make_animal("bird", "Gosha", "Parrot")
#     animal_from_fabric.commands = ["sing", "talk"]
#     print(animal_from_fabric)
#     print(*animal_from_fabric.commands)

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


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"bird": Birds, "reptile": Reptiles, "fish": Fishes}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("bird", "Gosha", "Parrot")
    animal_from_fabric.commands = ["sing", "talk"]
    print(animal_from_fabric)
    print(*animal_from_fabric.commands)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError("Invalid animal type")


if __name__ == '__main__':
    factory = AnimalFactory()
    animal1 = factory.create_animal("dog", "Buddy")
    animal2 = factory.create_animal("cat", "Whiskers")

    print(animal1.name)  # Output: Buddy
    print(animal1.speak())  # Output: Woof!

    print(animal2.name)  # Output: Whiskers
    print(animal2.speak())  # Output: Meow!
