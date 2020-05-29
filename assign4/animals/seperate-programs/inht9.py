#Multiple inheritance

class Lion:

	def __init__(self, name,power,species,trait):
		self.name = name
		self.power=power
		self.species = species
		self.trait=trait

	def walk(self):
        	return 'I am walking using'

	def charge(self):
        	return 'I charge from the back'



class Dog:

	def __init__(self, height, weight, species=None):
        	self.species = species
        	self.height = height
        	self.weight = weight

	def eat(self):
        	return "I'm eating"

	def sleep(self):
        	return "I'm sleeping"

	def walk(self):
        	return "I'm walking with my legs"


class LeoDog(Lion, Dog):

	def __init__(self, name, power, species,trait,height,weight):
        	Lion.__init__(self, name, power,species,trait)
        	Dog.__init__(self, height, weight)




p = LeoDog('Tommy', 'strong', 'Mammal', 'Dominative', '5','35')

print(p.walk())

