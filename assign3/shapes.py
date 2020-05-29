import turtle
tk=turtle.Turtle()
import time
class Deca:
	def __init__(self):
		self.length=85
		self.sides=10
		self.angle=360/self.sides
		print("Decagon")

	def draw(self):
		tk.color("purple")
		tk.begin_fill() 

		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)
		tk.end_fill()

		turtle.done()


class Nona:
	def __init__(self):
		self.length=85
		self.sides=9
		self.angle=360/self.sides
		print("Nonagon")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		time.sleep(2)

class Hepta:
	def __init__(self):
		self.length=85
		self.sides=7
		self.angle=360/self.sides
		print("Heptagon")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		

class Hex:
	
	def __init__(self):
		self.num_sides = 6
		self.side_length = 50
		self.angle = 360.0 / self.num_sides
		print("Hexagon")

	def get_side(self):

		side_length=int(input("Enter new side"))
		return side_length 
				
			
		
	def draw(self):
		for i in range(self.num_sides): 
			tk.forward(self.side_length) 
			tk.right(self.angle)



class Penta:
	def __init__(self):
		self.length=85
		self.sides=5
		self.angle=360/self.sides
		print("Pentagon")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)


class Tri:
	def __init__(self):
		self.length=85
		self.sides=3
		self.angle=360/self.sides
		print("Triangle")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)


class Octa:
	def __init__(self):
		self.length=85
		self.sides=8
		self.angle=360/self.sides
		print("Octagon")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)


class squ:
	def __init__(self):
		self.length=85
		self.sides=4
		self.angle=360/self.sides
		print("Square")

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

class Cube3D:
	
	def __init__(self):
		print("Cube3d")	
		 

	def draw(self):
		tk.color("grey") 
		tk.begin_fill() 
		tk.left(45) 
		tk.forward(100)
		tk.right(135) 
		tk.forward(100) 
		tk.right(45) 
		tk.forward(100) 
		tk.right(135) 
		tk.forward(100) 
		tk.end_fill() 

		# left side 
		tk.color("black") 
		tk.begin_fill() 
		tk.left(45) 
		tk.forward(100) 
		tk.left(135) 
		tk.forward(100) 
		tk.left(45) 
		tk.forward(100) 
		tk.left(135) 
		tk.forward(100) 
		tk.end_fill() 

		# top side 
		tk.color("blue") 
		tk.begin_fill() 
		tk.left(45) 
		tk.forward(100) 
		tk.right(90) 
		tk.forward(100) 
		tk.right(90) 
		tk.forward(100) 
		tk.right(90) 
		tk.forward(100) 
		tk.right(135) 
		tk.forward(100) 
		tk.end_fill()
		time.sleep(2)

class Star:
	def __init__(self):
		self.x=50
		self.y=144
		print("Star")
	def draw(self):
		for i in range(5): 
    			tk.forward(100) 
    			tk.right(144) 
      		
		
tk.color("black","yellow")
tk.begin_fill() 
st=Star()
st.draw()
tk.end_fill()
time.sleep(2)
tk.reset()

c=Cube3D()
c.draw()
tk.reset()		

tk.color("black","blue")
tk.begin_fill() 
sq=squ()
sq.draw()
tk.end_fill()
time.sleep(2)
tk.reset()

		

tk.color("green")
tk.begin_fill() 
non=Penta()
non.draw() 
tk.end_fill()
time.sleep(2)
tk.reset()
		

tk.color("red")
tk.begin_fill() 
h=Hex()
h.draw()
tk.end_fill()
time.sleep(2)
tk.reset()

tk.color("orange")
tk.begin_fill() 
penta=Hepta()
penta.draw()
tk.end_fill()
time.sleep(2)
tk.reset()

tk.color("pink")
tk.begin_fill() 
nona=Nona()
nona.draw()
tk.end_fill()
time.sleep(2)
tk.reset()

 
deca=Deca()
deca.draw()

		



