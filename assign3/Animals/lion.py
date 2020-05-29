class Lion:

	species='Mammal'


	def __init__(self,legs,food,fur,voice):
		self.legs=legs
		self.food=food
		self.fur=fur
		self.voice=voice


	def voicee(self):
		return "a lion {} in the jungle ".format(self.voice)



simba=Lion(4,"meat","brown","roars")
print(simba.voicee())
