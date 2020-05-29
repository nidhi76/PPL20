import turtle
tk=turtle.Turtle()


class Tri:
	def __init__(self):
		self.length=85
		self.sides=3
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			
			tk.left(self.angle)
			tk.forward(self.length)
			

		turtle.done()


tri=Tri()
tri.draw()
