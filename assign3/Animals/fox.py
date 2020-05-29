class Fox:
	species="Mammal"

	def __init__(self,name,eat,fur,legs,noise):
		self.name=name
		self.eat=eat
		self.fur=fur
		self.noise=noise
		self.legs=legs

	def speak(self,sound):
		return 'what does the fox say {}'.format(sound)

cunning=Fox("Jack","grass","brown",4,"meow")
print(Fox.species)
print(cunning.speak("arrh"))

