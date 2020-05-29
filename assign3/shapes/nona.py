import turtle
tk=turtle.Turtle()


class Nona:
	def __init__(self):
		self.length=85
		self.sides=9
		self.angle=360/9

	def draw(self):
		for i in range(self.sides):
			tk.left(self.angle)
			tk.forward(self.length)

		turtle.done()


nona=Nona()
nona.draw()
