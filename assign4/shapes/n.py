from abc import ABC, abstractmethod
import turtle 
import math
import time
t = turtle.Turtle()
t.speed(1.5)

class Shapes(ABC):

	def __init__(self):
		self.shapes = True


	def draw(self):
		pass

  
	def type(self):
		pass


	def perimeter(self):
		pass

class Deca(Shapes):


	def __init__(self):
		Shapes.__init__(self)
		self.length=85
		self.sides=10
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)



	def perimeter(self):
		print("Perimeter of decagon is {}".format(self.length*self.sides))
			
	


class Rectangle(Shapes):

	def __init__(self):
		Shapes.__init__(self)
		self.length = 85
		self.breadth = 170


	def draw(self):
		t.forward(self.length)
		t.left(90)
		t.forward(self.breadth)
		t.left(90)
		t.forward(self.length)
		t.left(90)
		t.forward(self.breadth)



	def perimeter(self):
		print("Perimeter of rectangle is {}".format(2*(self.length+self.breadth)))
		
    

class Triangle(Shapes):

	def __init__(self):
		Shapes.__init__(self)
		self.length=85
		self.sides=3
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)


	def perimeter(self):
		print("Perimeter of triangle is {}".format(3*(self.length)))
		
			


class Pentagon(Shapes):


	def __init__(self):
		self.length=85
		self.sides=5
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)



	def perimeter(self):
		print("Perimeter of Pentagon is {}".format(5*(self.length)))

		

class Circle(Shapes):

	def __init__(self):
		Shapes.__init__(self)
		self.rad = 100

	def draw(self):
		t.circle(self.rad)


	def perimeter(self):
		print("Perimeter of circle is {}".format(2*math.pi*self.rad))
    


class Hexagon(Shapes):

	def __init__(self):
		self.length=85
		self.sides=6
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)


	def perimeter(self):
		print("Perimeter of Hexagon is {}".format(6*(self.length)))

		
class Heptagon(Shapes):

	def __init__(self):
		self.length=85
		self.sides=7
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)


	def perimeter(self):
		print("Perimeter of Heptagon is {}".format(7*(self.length)))


class Octagon(Shapes):

	def __init__(self):
		self.length=85
		self.sides=8
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			t.left(self.angle)
			t.forward(self.length)


	def perimeter(self):
		print("Perimeter of Octagon is {}".format(8*(self.length)))



class Cube3D(Shapes):

	def __init__(self):
		self.l1=45
		self.l2=100
		self.l3=135
		self.l4=90
	
	
	def draw(self):
		t.color("grey") 
		t.begin_fill() 
		t.left(self.l1) 
		t.forward(self.l2)
		t.right(self.l3) 
		t.forward(self.l2) 
		t.right(self.l1) 
		t.forward(self.l2) 
		t.right(self.l3) 
		t.forward(self.l2) 
		t.end_fill() 

		# left side 
		t.color("black") 
		t.begin_fill() 
		t.left(self.l1) 
		t.forward(self.l2) 
		t.left(self.l3) 
		t.forward(self.l2) 
		t.left(self.l1) 
		t.forward(self.l2) 
		t.left(self.l3) 
		t.forward(self.l2) 
		t.end_fill() 

		# top side 
		t.color("blue") 
		t.begin_fill() 
		t.left(self.l1) 
		t.forward(self.l2) 
		t.right(self.l4) 
		t.forward(self.l2) 
		t.right(self.l4) 
		t.forward(self.l2) 
		t.right(self.l4) 
		t.forward(self.l2) 
		t.right(self.l3) 
		t.forward(self.l2) 
		t.end_fill()
		time.sleep(2)



	def vol(self):
		print("Volume of cube {}" .format(self.l1*self.l2*self.l3))

class Star(Shapes):
	def __init__(self):
		self.x=50
		self.y=144
	def draw(self):
		for i in range(5): 
    			t.forward(100) 
    			t.right(144) 
      
		
 



