import turtle
skk=turtle.Turtle()

class star:
	def __init__(self):
		self.x=50
		self.y=144
	def draw(self):
		for i in range(5): 
    			skk.forward(100) 
    			skk.right(144) 
      
		turtle.done()
 

s=star()
s.draw()
