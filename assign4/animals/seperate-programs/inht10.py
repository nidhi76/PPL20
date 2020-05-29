#Diamond inheritance
class Lion:

	 def class_names(self):
        	print( 'I am the king of the jungle')


class Rat(Lion):

	def class_names(self):
		super().class_names()
		print( 'I am rat ')


class Deer(Lion):

	def class_names(self):
		super().class_names()
		print('I am Deer')


class Goat(Lion):

        def class_names(self):
                super().class_names()
                print('I am Goat')


class Dog(Deer,Rat,Goat):

	def class_names(self):
		super().class_names()
		print( 'I am dog')


obj_c = Dog()

obj_c.class_names()

