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



class Lion:

	species='Mammal'


	def __init__(self,legs,food,fur,voice):
		self.legs=legs
		self.food=food
		self.fur=fur
		self.voice=voice


	def voicee(self):
		return "a lion {} in the jungle ".format(self.voice)




class Pigeon:
	def __init__(self,name):
		self.name=name
		self.db=self.cuckoo()


	class cuckoo:
		def __init__(self):
			self.dd="03"
			self.mm="09"
			self.yy="1989"
			

		def display(self):
			print('{}/{}/{} is your DOB'.format(self.dd,self.mm,self.yy))






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



class Sprw:
	def __init__(self):
		self.name='Charles'

	def display(selef):
		print("Name",self.name)


	class Hawk:


		def __init__(self):
			self.dd='09'
			self.mm='09'
			self.yy='1999'

		def display(self):
			print('Dob {}/{}/{}/'.format(self.dd,self.mm,self.yy))



p=Sprw()
x=Sprw().Hawk()
x.display()



obj1=Robin("grains","jack","black")
obj1.set_name()
Robin.fly("Robin")
obj1.print_name()
print(str(obj1._Robin__no)+' is a private variable' ) #name mangling /displaying private variables

 


gilch=Puma("David",34)
print(gilch.get_name())
print(gilch.get_age())
print(gilch.set_name())





pige=Pigeon("Arthur")
x=pige.db
x.display()



simba=Lion(4,"meat","brown","roars")
print(simba.voicee())



cunning=Fox("Jack","grass","brown",4,"meow")
print(Fox.species)
print(cunning.speak("arrh"))



e=Eagle("Hawkeye",23)
Vulture.mymethod(e)
e.display()



obj1=Dove("grains","jack","gray")
obj1.set_name()
Dove.fly("Pigeon")
obj1.print_name()
#Dove.eatt("Pigeons","Grains")



philo=Dog("GOOFY",23,4,"pedigree")
print(Dog.fullname(philo))
print(Dog.eatt(philo))


tom=Cat("goldy",4,"fish","meow","white")

print(Cat.fur(tom))

