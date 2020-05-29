
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print( 'blah blah')


class Dog(Animal):
    def __init__(self, name, species, color):
        super().__init__(name,species)
        self.color = color

    def speak(self):
        print('bow bow')


class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)

    def speak(self):
        print('meow meow')

snow = Dog('snow', 'mammal', 'white')
oscar = Cat('oscar', 'mammal','green')


snow.speak()
oscar.speak()
