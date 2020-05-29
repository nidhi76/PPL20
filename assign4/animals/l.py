
from abc import ABC, abstractmethod

class Animals(ABC):                    
	def __init__(self):
		self.eyes = 2
		self.legs = 4
		self.neck = 1

	def type(self):
		print("All mammals/humans/birds are all animals")

	@abstractmethod
	def setsound(self, sound):
		pass

	@abstractmethod
	def getsound(self):
		pass

class Interface(ABC):                     
	@abstractmethod
	def attack(self):
		pass

	@abstractmethod
	def extinct(self):
		pass


class Single(Animals):
    
	def poly(self):
		print('likes meat')

class Lion(Interface, Single):                    

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan

	def color(self):
		print("Yellow")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A lion makes  {}  sound.".format(self.sound))

	def type(self):
		print("Carnivore")

	def attack(self):
		print("Attacks from back")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan


class Tiger(Interface, Single):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan

	def color(self):
		print("Orange,black marks")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Tiger makes  {}  sound.".format(self.sound))
		

	def type(self):
		print("Carnivore")

	def attack(self):
		print("Attacks from front")

	def extinct(self):
		print("No, Tiger is not extinct.")

	def ret_lifespan(self):
		return self.lifespan

class Sphinx(Single, Interface):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan


	def eats(self):                        
		print("These cats do not tolerate poor quality food or frequent diet")

	def color(self):
		print("They are hairless,hence appear white or very light")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Sphinx makes  {}  sound.".format(self.sound))


	def typeOfAnimal(self):
		print("Carnivore")

	def attack(self):
		print("Doesnt attack")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan

class Giraffe(Animals, Interface):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan
	
	def eats(self):
		print("Eats Leaves")

	def color(self):
		print("Yellow in colour with dark patches")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Giraffe makes  {}  sound.".format(self.sound))


	def attack(self):
		print("Doesnt attack")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan


class Eagle(Animals, Interface):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan

	def eats(self):
		print("small animals/insects")
	
	def color(self):
		print("white features on neck with dark on the body")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Giraffe makes  {}  sound.".format(self.sound))

	def attack(self):
		print("No")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan


class Vulture(Animals, Interface):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan

	def eats(self):
		print("Feeds on dead ")

	def color(self):
		print("dark feathers with white feathers on neck")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Giraffe makes  {}  sound.".format(self.sound))


	def attackHumans(self):
		print("No")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan


class Robin(Animals, Interface):

	def __init__(self, lifespan):
		Animals.__init__(self)
		self.lifespan = lifespan

	def eats(self):
		print("Smalls insects")

	def color(self):
		print("dark feathers")

	def setsound(self, sound):
		self.sound = sound

	def getsound(self):
		print("A Giraffe makes  {}  sound.".format(self.sound))


	def type(self):
		print("carnivore")

	def attackHumans(self):
		print("No")

	def extinct(self):
		print("No")

	def ret_lifespan(self):
		return self.lifespan


class Sprw(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("tiny insects")

    def color(self):
        print("light brown")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A sparrow makes  {}  sound.".format(self.sound))

    def type(self):
        print("Eats insects")

    def attack(self):
        print("No")

    def extinct(self):
        print("No")

    def ret_lifespan(self):
        return self.lifespan

class Puma(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("meat")

    def color(self):
        print("dark purple")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A puma makes  {}  sound.".format(self.sound))

    def type(self):
        print("Omnivore")

    def attack(self):
        print("No")

    def extinct(self):
        print("No")

    def ret_lifespan(self):
        return self.lifespan







