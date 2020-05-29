import turtle
tk=turtle.Turtle()


class Deca:
	def __init__(self):
		self.length=85
		self.sides=10
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		turtle.done()


deca=Deca()
deca.draw()
