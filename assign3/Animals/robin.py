class Robin:
	wings=2
	def __init__(self,eat,name,colour):

		self.name=name
		self.eat=eat
		self.colour=colour
		self.__no=34
	def set_name(self):
		new_name=input("Enter a name:")
		self.name=new_name

	def print_name(self):
		print(' {} is the new name '.format(self.name))

	@classmethod
	def fly(cls,name):
		print('{} flies with {} wings'.format(name,Robin.wings))



obj1=Robin("grains","jack","black")
obj1.set_name()
Robin.fly("Robin")
obj1.print_name()
print(str(obj1._Robin__no)+' is a private variable' ) #name mangling /displaying private variables

