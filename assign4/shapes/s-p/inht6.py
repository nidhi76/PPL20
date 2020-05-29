class rec:

	all_sides_equal=False	
	opp_sides_equal=True
	sides=4
	type='quadrilateral'

	def area(self):
		print("This is for rectangle ")
		l=int(input("Enter length: "))
		b=int(input("Enter breadth: "))
		print( "Area of rectangle is {}".format(l*b))



class square(rec):

	sides_equal=True

	def area(self):
		super().area()
		print("This is for square")
		l=int(input("Enter length: "))
		print("Area of square: {}".format(l*l))



r=square()
r.area()
print("Sides of a square: {}".format(r.sides_equal))
print("Square is a: {}".format(r.type))
print("Rectangle is a: {}".format(rec.type))
print("Are all sides equal in rectangle: {}".format(r.all_sides_equal))
print("Are all sides equal in square: {}".format(r.sides_equal))
