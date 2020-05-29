import turtle
tk=turtle.Turtle()


class Penta:
	def __init__(self):
		self.length=85
		self.sides=5
		self.angle=360/5

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		turtle.done()


penta=Penta()
penta.draw()
