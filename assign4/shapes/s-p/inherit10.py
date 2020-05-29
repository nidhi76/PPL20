#Diamond inheritance
class quad:

	 def class_names(self):
        	print( 'I am the king of the jungle')


class square(quad):

	def class_names(self):
		super().class_names()
		print( 'I am rat ')


class rectangle(quad):

	def class_names(self):
		super().class_names()
		print('I am Deer')


class rhombus(quad):

        def class_names(self):
                super().class_names()
                print('I am Goat')


class kite(rectangle,rhombus,kite):

	def class_names(self):
		super().class_names()
		print( 'I am dog')


obj_c = Dog()

obj_c.class_names()

