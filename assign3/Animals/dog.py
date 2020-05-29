class Dog:

	def __init__(self,name,age,legs,eat):
		self.name=name
		self.age=age
		self.legs=legs
		self.eat=eat

	def fullname(self):
		return ' {} '.format(self.name)


	def eatt(self):
		return ' {} '.format(self.eat)


philo=Dog("GOOFY",23,4,"pedigree")
print(Dog.fullname(philo))
print(Dog.eatt(philo))







