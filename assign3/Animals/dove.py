class Dove:
	wings=2
	def __init__(self,eat,name,colour):

		self.name=name
		self.eat=eat
		self.colour=colour

	def set_name(self):
		new_name=input("Enter a name:")
		self.name=new_name

	def print_name(self):
		print(' {} is the new name '.format(self.name))

	@classmethod
	def fly(cls,name):
		print('{} flies with {} wings'.format(name,Dove.wings))



obj1=Dove("grains","jack","gray")
obj1.set_name()
Dove.fly("Pigeon")
obj1.print_name()
#Dove.eatt("Pigeons","Grains")
