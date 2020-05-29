class Square:
	def __init__(self,x):
		self.x=x
	def area(self):
		print("Area",self.x*self.x)


class Rectangle(Square):

	def __init__(self,x,y):
		super().__init__(x)
		self.y=y

	def area(self):
		super().area()
		print("Area of Rectangle {}".format(self.x*self.y))


rec=Rectangle(12,13)
rec.area()

