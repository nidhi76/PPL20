import turtle
polygon = turtle.Turtle() 


class quad:
	def __init__(self,sides,length):
		self.sides = sides
		self.length = length
		self.angle = 360.0 / sides




class shape(quad):

	def __init__(self,sides,length):
		super().__init__(sides,length)

	def draw(self):
		for i in range(self.sides):
			polygon.forward(self.length)
			polygon.right(self.angle)
		turtle.done()
		polygon.fillcolor(red) 
  		





p=int(input("Enter no of sides"))
q=int(input("Enter the  length"))

f=shape(p,q)
f.draw()
turtle.reset()


p=int(input("Enter no of sides"))
q=int(input("Enter the  length"))

