class Eagle:

	def __init__(self,name,eat):
		self.name=name
		self.eat=eat
		
	
	def display(self):
		print("Using staticmethod to increment eat variable.Value of eat variable is {}".format(self.eat))

class Vulture:

	@staticmethod
	def mymethod(e):
		e.eat+=4 


e=Eagle("Hawkeye",23)
Vulture.mymethod(e)
e.display()
