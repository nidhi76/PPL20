class Cat:
	def __init__(self,name,legs,eat,noise,furr):
		self.name=name
		self.legs=legs
		self.eat=eat
		self.noise=noise
		self.furr=furr


	def eatt(self):
		return '{} '.format(self.eat)


	def talk(self):
		
		return '{}'.format(self.noise)


	def fur(self):
		
		return '{}'.format(self.furr)




tom=Cat("goldy",4,"fish","meow","white")

print(Cat.fur(tom))

