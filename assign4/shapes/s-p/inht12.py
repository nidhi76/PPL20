class Shape(object):


	def __init__(self, sides):
        	self.sides = sides

	def perimeter(self):
        	perimeter = 0
        	for side in self.sides:
            		perimeter += side
        	return perimeter

	
class Triangle(Shape):
    	def __init__(self, side1, side2, side3):
        	self.sides = [side1, side2, side3]

class Rectangle(Shape):
	def __init__(self, length, width):
		self.sides = [length, width, length, width]
		self.area=length*width
class Square(Shape):
	def __init__(self, side):
		self.sides = [side, side, side, side]
		self.area=side*side
triangle = Triangle(3, 4, 5)
print("triangle sides:", triangle.sides)
print("triangle perimeter:", triangle.perimeter())

rectangle = Rectangle(4, 2)
print("rectangle sides:", rectangle.sides)
print("rectangle perimeter:", rectangle.perimeter())
print("Area rectangle:",rectangle.area)
square = Square(2)
print("square sides:", square.sides)
print("square perimeter:", square.perimeter())
print("Area square ",square.area)
