#Here the pigeon class inherits the constructor of Eagle Class
#Also there is class and method overriding
class Eagle:
	def __init__(self):
		self.wings=2
		self.eyes=2
		self.nose=1
		self.legs=2

	def eat(self,food):
		self.food=food

	def food_print(self):
		print("Eagle eats {} ".format(self.food))

class Pigeon(Eagle):
	
	def ret_print(self):
		print('A pigeon has {} eyes ,{} legs {} nose'.format(self.eyes,self.legs,self.nose))


	def eat(self,food):
		self.food=food

	def food_print(self):
		print("Pigeon eats {}".format(self.food))


p=Pigeon()
p.eat("Grains")
p.food_print()
p.ret_print()
