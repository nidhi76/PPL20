class Puma:
	def __init__(self,name,age):
		self.name=name
		self.age=age


	def get_name(self):
		return 'name is {} '.format(self.name)


	def get_age(self):
		return 'age is {} '.format(self.age)


	def set_name(self):
		new_name=input("enter new name:")
		self.name=new_name
		return 'new name is {} '.format(self.name)


	def set_age(self,new_age):
		self.age=new_age
		return 'new age is {} '.format(self.age)
 


gilch=Puma("David",34)
print(gilch.get_name())
print(gilch.get_age())
print(gilch.set_name())


