import turtle
tk=turtle.Turtle()



class Octagon:

	def __init__(self):
		self.length=70
		self.sides=8
		self.angle=360/self.sides

	def draw(self):
		
		for i in range(self.sides):
			tk.forward(self.length)
			tk.right(self.angle)
		
		turtle.done()

octa=Octagon()
octa.draw()
		
