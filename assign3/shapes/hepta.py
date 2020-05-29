import turtle
tk=turtle.Turtle()


class Hepta:
	def __init__(self):
		self.length=85
		self.sides=7
		self.angle=360/self.sides

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		turtle.done()


penta=Hepta()
penta.draw()
